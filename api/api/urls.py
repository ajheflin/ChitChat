"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path
from chitchatapi import views
#hello
urlpatterns = [
    #admin/
    path('admin/', admin.site.urls),
    #users/
    path("users/", views.ListUsers.as_view()),
    #messages/chat/{chatid}
    re_path("messages/chat/(?P<Chat>.+)/$", views.ListMessagesForChat.as_view()),
    #users/{userid}
    re_path("users/(?P<UID>.?)/$", views.GetUserInfo.as_view()),
    #users/{userid}/chats
    re_path("users/(?P<UID>.+)/chats/$", views.ListChatsForUser.as_view()),
    #chats/{chatid}
    re_path("chats/(?P<chatid>.?)/$", views.ListChatById.as_view()),
    #chats/
    path("chats/", views.ListChats.as_view()),
    #messages/
    path("messages/", views.ListMessages.as_view()),
    #users/manage
    path('users/manage', views.UserManage.as_view()),
    #chats/manage
    path('chats/manage', views.ChatManage.as_view()),
    #messages/manage
    path('messages/manage', views.MessageManage.as_view())
]
