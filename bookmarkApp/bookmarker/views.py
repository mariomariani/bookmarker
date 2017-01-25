from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login

def auth(request):
    errors = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password,
            errors=errors)
        if user is not None:
            print user
            print '------{0}'.format(user.token)
            login(request, user)
            if user.is_superuser:
                return redirect('users/index.html')
            return redirect('bookmarker:index')

    return render(request, 'login.html', 
        {'error_message': ', '.join(errors)})

@login_required
def index(request):
    bookmarks = [1, 2, 3]
    context = {
        'bookmarks': bookmarks,
    }
    return render(request, 'bookmarks/index.html', context)

def create(request):
    request.POST['url']
    HttpResponseRedirect(reverse('bookmarker:index'))

def detail(request, bookmark_id):
    bookmarks = [1, 2, 3]
    try:
        bookmark = bookmarks[int(bookmark_id)]
    except:
        raise Http404("Bookmark not found.")
    return render(request, 'bookmarks/detail.html', { 'bookmark': bookmark })
