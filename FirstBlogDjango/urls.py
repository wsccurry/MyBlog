"""FirstBlogDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from article import views
from user.views import login
from user.views import register
from user.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/(?P<id>\d+)/$',views.detail,name='detail'),
    url(r'^$',views.home,name='home'),
    url(r'^aboutme/$',views.about_me,name='aboutme'),
    url(r'^tags/$',views.tags,name='tags'),
    url(r'^tags/(?P<tag>\w+)/$',views.search_tag,name='search_tag'),
    url(r'^select/$',views.select,name='select'),
    url(r'^feed/$',views.RSSFeed(),name='RSS'),
    url(r'^login/$',login,name='login'),
    url(r'^register/$',register,name='register'),
    url(r'^logout/$',logout,name='logout')
]
