from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from bookmarker.services import BookmarkService

def auth(request):
    errors = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password,
            errors=errors)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('users/index.html')
            return redirect('bookmarker:index')

    return render(request, 'login.html', 
        {'error_message': ', '.join(errors)})

@login_required
def index(request):
    service = BookmarkService()

    # service.addBookmark(request.user, '')

    bookmarks = service.getUserBookmarks(request.user)

    for bookmark in bookmarks:
        bookmark['id'] = bookmark['_id']

    context = {
        'bookmarks': bookmarks,
    }
    return render(request, 'bookmarks/index.html', context)

def create(request):
    request.POST['url']
    HttpResponseRedirect(reverse('bookmarker:index'))

def detail(request, bookmark_id):
    service = BookmarkService()
    bookmark = service.getBookmark(bookmark_id)
    if not bookmark:
        return Http404("Bookmark not found.")
    return render(request, 'bookmarks/detail.html', { 'bookmark': bookmark })
