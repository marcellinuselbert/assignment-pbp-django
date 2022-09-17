from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList


def show_watchlist_index(request):
    return render(request, 'index_watchlist.html')

def show_watchlist(request):
    watch_list = MyWatchList.objects.all()
    context = {
    'name': 'Marcellinus Elbert',
    'student_id': '2106752400',
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