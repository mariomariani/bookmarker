from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

def index(request):
    bookmarks = [1, 2, 3]
    context = {
        'bookmarks': bookmarks,
    }
    return render(request, 'bookmarks/index.html', context)

def detail(request, bookmark_id):
    bookmarks = [1, 2, 3]
    try:
        bookmark = bookmarks[int(bookmark_id)]
    except:
        raise Http404("Bookmark not found.")
    return render(request, 'bookmarks/detail.html', { 'bookmark': bookmark })

def results(request, bookmark_id):
    response = "You're looking at the results of bookmark %s."
    return HttpResponse(response % bookmark_id)

def vote(request, bookmark_id):
    return HttpResponse("You're voting on bookmark %s." % bookmark_id)