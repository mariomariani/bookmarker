from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from bookmarker.services import BookmarkService, merge_errors

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

    return render(request, 'login.html', merge_errors(errors))

@login_required
def index(request):
    service = BookmarkService()
    
    if request.method == 'POST':
        bookmark = { 'url': request.POST['url'] }
        service.addBookmark(request.user, bookmark)
        return redirect('bookmarker:index')

    bookmarks = service.getUserBookmarks(request.user)

    context = { 'bookmarks': bookmarks }
    return render(request, 'bookmarks/index.html', context)

@login_required
def edit(request, bookmark_id):
    service = BookmarkService()

    if request.method == 'GET':
        bookmark = service.getBookmark(user=request.user,
            bookmark_id=bookmark_id)
        
        if not bookmark:
            return Http404("Bookmark not found.")
        
        context = { 'bookmark': bookmark }
        return render(request, 'bookmarks/edit.html', context)

    if request.method == 'POST':
        bookmark = {
            'id': bookmark_id,
            'url': request.POST['url'],
        }
        service.updateBookmark(request.user, bookmark)
        
        return redirect('bookmarker:index')

