from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList


def show_watchlist_index(request):
    watch_list = MyWatchList.objects.all()
    watched_count = 0
    not_watched_count = 0
    result = False

    for movie in watch_list:
        if movie.watched:
            watched_count += 1
        else:
            not_watched_count += 1

    if watched_count >= not_watched_count:
        result = True 

    context = {
        'is_watching_a_lot': result
    }


    return render(request, 'index_watchlist.html', context)

def show_watchlist(request):
    watch_list = MyWatchList.objects.all()
    context = {
    'watch_list': watch_list
    }
    return render(request, 'watchlist.html',context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("html", data), content_type="application/html")