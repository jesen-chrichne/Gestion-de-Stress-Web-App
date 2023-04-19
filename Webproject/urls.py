"""Webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from Webapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_admin/', views.index_admin, name='index_admin'),
    path('index_app/', views.index_app, name='index_app'),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profil/', views.profil, name='profil'),
    path('create_comment/<id>', views.create_comment, name='create_comment'),
    path('ressource_app/', views.ressource_app, name='ressource_app'),
    path('manage_stress_app/', views.manage_stress_app, name='manage_stress_app'),
    path('journal_app/', views.journal_app, name='journal_app'),
    path('pub_post_user/', views.pub_post_user, name='pub_post_user'),
    path('details_pub/<id>/', views.details_pub, name='details_pub'),
    path('like_post/<id>', views.like_post, name='like_post'),
    path('assistance/', views.assistance, name='assistance'),
    path('profil_user/<id>/', views.profil_user, name='profil_user'),
    path('cas/<id>/', views.cas, name='cas'),
    path('non_cas/<id>/', views.non_cas, name='non_cas'),
    path('chat/', views.chat, name='chat'),
    path('chat_mp/<str:room>', views.chat_mp, name='chat_mp'),
    path('send', views.send, name='send'),
    # path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('send_msg/', views.send_msg, name='send_msg'),
    path('update_user_app/<id>/', views.update_user_app, name='update_user_app'),
    
    path('news_post_admin/', views.news_post_admin, name='news_post'),
    path('add_news_post_admin/', views.add_news_post_admin, name='add_news_post_admin'),
    path('create_news_post_admin/', views.create_news_post_admin, name='create_news_post_admin'),
    path('edit_news_post_admin/<id>/', views.edit_news_post_admin, name='edit_news_post_admin'),
    path('update_news_post_admin/<id>/', views.update_news_post_admin, name='update_news_post_admin'),
    path('delete_news_post_admin/<id>/', views.delete_news_post_admin, name='delete_news_post_admin'),
    
    
    path('ressources_admin/', views.ressources_admin, name='ressources_admin'),
    path('add_ressource_admin/', views.add_ressource_admin, name='add_ressource_admin'),
    path('create_ressource_admin/', views.create_ressource_admin, name='create_ressource_admin'),
    path('edit_ressource_admin/<id>/', views.edit_ressource_admin, name='edit_ressource_admin'),
    path('update_ressource_admin/<id>/', views.update_ressource_admin, name='update_ressource_admin'),
    path('delete_ressource_admin/<id>/', views.delete_ressource_admin, name='delete_ressource_admin'),
    
    path('manage_stress_admin/', views.manage_stress_admin, name='manage_stress_admin'),
    path('add_manage_stress_admin/', views.add_manage_stress_admin, name='add_manage_stress_admin'),
    path('create_manage_stress_admin/', views.create_manage_stress_admin, name='create_manage_stress_admin'),
    path('edit_manage_stress_admin/<id>/', views.edit_manage_stress_admin, name='edit_manage_stress_admin'),
    path('update_manage_stress_admin/<id>/', views.update_manage_stress_admin, name='update_manage_stress_admin'),
    path('delete_manage_stress_admin/<id>/', views.delete_manage_stress_admin, name='delete_manage_stress_admin'),
    
    path('user_admin/', views.user_admin, name='user_admin'),
    path('add_user_admin/', views.add_user_admin, name='add_user_admin'),
    path('create_user_admin/', views.create_user_admin, name='create_user_admin'),
    path('edit_user_admin/<id>/', views.edit_user_admin, name='edit_user_admin'),
    path('update_user_admin/<id>', views.update_user_admin, name='update_user_admin'),
    path('delete_user_admin/<id>/', views.delete_user_admin, name='delete_user_admin'),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
