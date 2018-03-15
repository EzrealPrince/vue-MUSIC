"""mytest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from songs import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('index',views.index,name='homepage'),
    path('add_song',views.add_song,name='add_song'),
    path('add_star',views.add_star,name='add_star'),
    path('view_song_list',views.view_song_list,name='view_song_list'),
    path('view_star_list',views.view_star_list,name='view_star_list'),
    path('delete',views.delete,name='delete'),
    path('view_song/detail', views.detail, name='detail'),
]
