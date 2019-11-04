"""book_sys URL Configuration

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
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    #出版社有关的url
    url(r'^add_publish/', views.add_publish),
    url(r'^publish_list/', views.publish_list),
    url(r'^del_publish/', views.del_publish),
    url(r'^edit_publish/', views.edit_publish),
    #书有关的url
    url(r'^add_book/', views.add_book),
    url(r'^book_list/', views.book_list),
    url(r'^edit_book/', views.edit_book),
    url(r'^del_book/', views.del_book),


    #作者相关
    url(r'^add_author/', views.add_author),
    url(r'^author_list/', views.author_list),
    url(r'^edit_author/', views.edit_author),
    url(r'^del_author/', views.del_author),

    #结束页
    url(r'^end/', views.end),
]
