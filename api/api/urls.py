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
urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", views.ListUsers.as_view()),
    re_path("messages/chat/(?P<Chat>.+)/$", views.ListMessagesForChat.as_view()),
    re_path("users/(?P<UID>.?)/$", views.GetUserInfo.as_view()),
    re_path("users/(?P<UID>.+)/chats/$", views.ListChatsForUser.as_view()),
    path("chats/", views.ListChats.as_view()),
    path("messages/", views.ListMessages.as_view())
]
