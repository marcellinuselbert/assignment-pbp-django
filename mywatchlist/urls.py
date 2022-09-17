from django.urls import path
from mywatchlist.views import show_watchlist, show_xml,show_json, show_html,show_watchlist_index

app_name = 'mywatchlist'

urlpatterns = [
    
    path('', show_watchlist_index, name="index"),
    path('xml',show_xml,name="show_xml"),
    path('json',show_json,name="show_json"),
    path('html',show_watchlist,name="show_html"),
]