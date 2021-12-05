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
from django.views.decorators.csrf import csrf_exempt
from chitchatapi import views
# hello
urlpatterns = [
    # admin/
    path('api/admin/', admin.site.urls),
    # users/
    path("api/users/", views.ListUsers.as_view()),
    # messages/chat/{chatid}
    re_path("api/messages/chat/(?P<Chat>.+)/$",
            views.ListMessagesForChat.as_view()),
    # users/{userid}
    re_path("api/users/(?P<UID>[0-9]+)/$", views.GetUserInfo.as_view()),
    # users/{userid}/chats
    re_path("api/users/(?P<UID>[0-9]+)/chats/$", views.ListChatsForUser.as_view()),
    # chats/
    path("api/chats/", views.ListChats.as_view()),
    re_path("api/chats/(?P<CID>[0-9]+)/$", views.GetChatInfo.as_view()),
    # messages/
    path("api/messages/", views.ListMessages.as_view()),
    # users/manage
    path('api/users/manage', views.UserManage.as_view()),
    # chats/manage
    path('api/chats/manage', views.ChatManage.as_view()),
    # messages/manage
    path('api/messages/manage', csrf_exempt(views.MessageManage.as_view())),
    re_path('api/users/username/(?P<username>\w+)',
            views.GetUserInfoByUsername.as_view()),
    path('api/auth/', csrf_exempt(views.AuthUser.as_view())),
    path('api/register/', csrf_exempt(views.Register.as_view())),
    path('api/chats/adduser', csrf_exempt(views.AddUserToChat.as_view())),
    path('api/chats/removeuser', csrf_exempt(views.RemoveUserFromChat.as_view())),
    re_path('api/users/delete/(?P<UID>.+)/$',
            csrf_exempt(views.DeleteUser.as_view())),
    path('api/users/changeUsername/', csrf_exempt(views.ChangeUsername.as_view())),
    path('api/users/changeName/', csrf_exempt(views.ChangeName.as_view())),
    path('api/users/changePassword/', csrf_exempt(views.ChangePassword.as_view()))
]
