from django.shortcuts import render
from user.models import User
from article.views import home
from django import forms
# Create your views here.
def login(request):
    if request.method=="POST":
        user=request.POST['user']
        password=request.POST['pass']
        if user and password:
            if User.objects.filter(user_name=user,pass_word=password):
                request.session['username']=user
                request.session['password']=password
                request.session.set_expiry(600) #session过期时间是600s
                return home(request)
    return render(request,"login.html")

def logout(request):
    if 'username' in request.session:
        del  request.session["username"]
    return home(request)

def register(request):
    if request.method=="POST":
        signForm=SignForm(request.POST)
        if signForm.is_valid():
            sign_info=signForm.cleaned_data
            username=sign_info['username']
            password=sign_info['password_1']
            User.objects.create(user_name=username,pass_word=password)
            return home(request)
        else:
            return render(request,"register.html",{'form':signForm}) #验证失败要返回
    signForm=SignForm()
    return render(request,"register.html",{'form':signForm})

class SignForm(forms.Form):
    username=forms.CharField(label="用户名:",max_length=10)
    password_1=forms.CharField(label="输入密码",max_length=10,widget=forms.PasswordInput)
    password_2=forms.CharField(label="确认密码",max_length=10,widget=forms.PasswordInput)

    def clean_username(self):
        username=self.cleaned_data.get('username')
        if User.objects.filter(user_name=username):
            raise forms.ValidationError("用户名已存在")
        return username

    def clean_password_2(self):
        password_1=self.cleaned_data.get('password_1')
        password_2=self.cleaned_data.get('password_2')
        if password_1 and password_2 and password_1!=password_2:
            raise forms.ValidationError("两个密码不一致")
        return password_2
