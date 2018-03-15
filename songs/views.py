from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django import forms
from django.contrib import auth
from django.urls import reverse
from songs.models import user,song,star
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.shortcuts import render

def login(request):
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            state = 'password_error'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None
    }
    return render(request, 'login.html', content)

def index(request): 
    content = {
          'active_menu':'homepage',
          
    }
    return render(request,'index.html',content)

def logout(request):
    auth.logout(request)
    state=None
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None
    }
    return render(request,'login.html',content)

def view_star_list(request):
    user = request.user
    song_list = song.objects.values_list('song_name', flat=True).distinct()
    query_name = request.GET.get('song_name', 'all')
    if (not query_name) or song.objects.filter(song_name=query_name).count() is 0:
        query_name = 'all'
        song_list = song.objects.all()
    else:
        song_list = song.objects.filter(song_author__star_name=query_name)

    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        song_list = song.objects.filter(song_author__star_name__contains=keyword)
        query_name = 'all'

    paginator = Paginator(song_list, 6)
    page = request.GET.get('page')
    try:
        song_list = paginator.page(page)
    except PageNotAnInteger:
        song_list = paginator.page(1)
    except EmptyPage:
        song_list = paginator.page(paginator.num_pages)
    content = {
        'user': user,
        'active_menu': 'view_star',
        'query_type': query_name,
        'song_list': song_list,
    }
    return render(request, 'view_song_list.html', content)

def view_song_list(request):
    user = request.user
    song_list = song.objects.values_list('song_name', flat=True).distinct()
    query_name = request.GET.get('song_name', 'all')  
    if (not query_name) or song.objects.filter(song_name=query_name).count() is 0:
        query_name = 'all'
        song_list = song.objects.all()
    else:
        song_list = song.objects.filter(song_name=query_name)

    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        song_list = song.objects.filter(song_name=keyword)
        query_name = 'all'

    paginator = Paginator(song_list, 6)
    page = request.GET.get('page')
    try:
        song_list = paginator.page(page)
    except PageNotAnInteger:
        song_list = paginator.page(1)
    except EmptyPage:
        song_list = paginator.page(paginator.num_pages)
    content = {
        'user': user,
        'active_menu': 'view_song',
        'query_type': query_name,
        'song_list': song_list,
    }
    return render(request, 'view_song_list.html', content)

def detail(request):
    user = request.user
    song_id = request.GET.get('id', '')
    if song_id == '':
        return HttpResponseRedirect(reverse('view_song_list'))
    try:
        songs = song.objects.get(pk=song_id)
    except songs.DoesNotExist:
        return HttpResponseRedirect(reverse('view_song_list'))
    content = {
        'user': user,
        'active_menu': 'view_song',
        'song': songs,
    }
    return render(request, 'detail.html', content)

def add_song(request):
    user = request.user
    state = None
    if request.method == 'POST':
        name = request.POST.get('song_author')
        stars = star.objects.get(star_name=name)
        new_song = song(
                song_name=request.POST.get('song_name', ''),
                song_author=stars,
                song_type=request.POST.get('song_type', ''),
                song_language=request.POST.get('song_language', ''),
                song_pinyin=request.POST.get('song_pinyin', '')
        )       
        new_song.save()
        state = 'success'
    content = {
        'user': user,
        'active_menu': 'add_song',
        'state': state,
    }
    return render(request, 'add_song.html', content)

def add_star(request):
    user = request.user
    state = None
    if request.method == 'POST':
        new_star = star(
                star_name=request.POST.get('star_name', ''),
                star_sex=request.POST.get('star_sex', ''),
                star_country=request.POST.get('star_country', ''),
                star_type=request.POST.get('star_type', ''),
                star_pinyin=request.POST.get('star_pinyin', '')
        )
        new_star.save()
        state = 'success'
    content = {
        'user': user,
        'active_menu': 'add_star',
        'state': state,
    }
    return render(request, 'add_star.html', content)

def delete(request):
    user = request.user
    state = None
    song_id = request.GET.get('id','')
    songs = song.objects.get(id=song_id).delete()
    song_list = song.objects.all()
    content = {
       'user':user,
       'active_menu':'view_song',
       'song_list':song_list,    
    }
    return render(request, 'view_song_list.html', content)

# Create your v
