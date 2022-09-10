from django.shortcuts import render
from katalog.models import CatalogItem
def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
    'name': 'Marcellinus Elbert',
    'student_id': '2106752400',
    'list_katalog': data_catalog_item
    }
    return render(request, 'katalog.html',context)
