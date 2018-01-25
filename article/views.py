from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from  article.models import Article
from  django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from datetime import datetime
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
from comment.views import show_comment
from comment.models import Comment
from user.models import User
#def short_text(all_article):
   # for article in  all_article:
       # if len(article.content)>=100:
          #  article.content=article.content[0:99]

def detail(request,id):
    try:
        post=Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    if request.method=='POST':
        if request.POST['c']:
            comment=request.POST['c']
            date_time=datetime.now()
            if 'username' in request.session:
                user_name=request.session['username']
                #pass_word=request.session['password']
                #if User.objects.filter(user_name=user_name,pass_word=pass_word):
                Comment.objects.create(user_name=user_name,titleId=id,date_time=date_time,content=comment)
            else:
                return HttpResponse('<script language=javascript>alert("登陆成功后才可评论");</script>')
    comments = show_comment(id)
    return render(request,'post.html',{'post':post,'comments':comments})


def home(request):
    all_article=Article.objects.all()
    #short_text(all_article)
    paginator=Paginator(all_article,3)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.paginator(paginator.num_pages)
    return render(request,'home.html',{'post_list':post_list})

def about_me(request):
    return render(request,'aboutme.html')

def search_tag(request,tag):
    try:
        post_list=Article.objects.filter(category=tag)
    except Article.DoesNotExist:
        raise Http404
   # short_text(post_list)
    return render(request, "search_tag.html", {'post_list':post_list})

def tags(request):
    all_tags=[]
    all_article=Article.objects.all()
    for article in all_article:
        tag=article.category
        if tag not in all_tags:
            all_tags.append(tag)
    return render(request,'tags.html',{'post_list':all_tags})

def select(request):
    if 's' in request.GET:
        s=request.GET['s']
    else:
        return render(request,'home.html')
    select_articles=Article.objects.filter(title__contains=s)
   # short_text(select_articles)
    return  render(request,'select.html',{'post_list':select_articles})

class RSSFeed(Feed):
    title='RSS feed - article'
    link='feeds/posts/'
    description='RSS feed - blog posts'
    def items(self):
        return Article.objects.order_by('-date_time')
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.content
    def item_pubdate(self,item):
        return datetime.strptime(str(item.date_time),'%Y-%m-%d')  #将数据库中的date类型datetime类型
    def item_link(self, item):
        return reverse('detail',kwargs={'id':item.id})
