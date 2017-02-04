from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from bookmarker.services import BookmarkService, merge_errors, UserService

def auth(request):
    if request.method == 'GET':
        if request.session:
            context = request.session.pop('context', None)
        return render(request, 'login.html', context)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        errors = []
        user = authenticate(username=username, password=password,
            errors=errors)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('users/index.html')
            return redirect('bookmarker:index')
        else:
            context = { 'error_message': merge_errors(errors) }
            return render(request, 'login.html', context)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    if request.method == 'POST':
        user_service = UserService()
        username = request.POST['username']
        password = request.POST['password']

        errors = []
        user = user_service.create_user(username, password, errors)
        
        if user:
            context = { 'message': 'User created successfully' }
            request.session['context'] = context
            # return render(request, 'login.html', context  )
            return redirect('bookmarker:login')
            # return render(request, 'signup.html', context)
        
        context = { 'error_message': merge_errors(errors) }
        return render(request, 'signup.html', context)

@login_required
def index(request):
    service = BookmarkService()
    
    if request.method == 'POST':
        bookmark = { 'url': request.POST['url'] }
        service.add_bookmark(request.user, bookmark)
        return redirect('bookmarker:index')

    bookmarks = service.get_user_bookmarks(request.user)

    context = { 'bookmarks': bookmarks }
    return render(request, 'bookmarks/index.html', context)

@login_required
def edit(request, bookmark_id):
    service = BookmarkService()

    if request.method == 'GET':
        bookmark = service.get_bookmark(user=request.user,
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
        service.update_bookmark(request.user, bookmark)
        
        return redirect('bookmarker:index')

