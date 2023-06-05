from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


menu = [{'title':'Администратор', 'url_name': 'adm'},
        {'title':'Войти', 'url_name': 'home'}]


def index(request):
    return render(request, 'main/index.html')
# указывая html шаблон, представляем, что мы уже находимся в папке template


def show_post(request, post_id):
    property = get_object_or_404(RealEstate, pk=post_id)

    context = {
        'property': property,
        'menu': menu,
        'title': property.title,
        'cat_selected': 1
    }
    return render(request, 'main/property.html', context=context)

def show_category(request, cat_id):
    property = RealEstate.objects.filter(type_id=cat_id)


    #if len(property) == 0:
    #    raise Http404()

    context = {
        'title': 'Список недвижимости определенного типа',
        'menu': menu,
        'real_estate': property,
        'cat_selected': cat_id,
    }
    return render(request, 'main/property_list.html', context=context)


def property_list(request):
    property = RealEstate.objects.all()

    context = {
        'title': 'Список недвижимости',
        'menu': menu,
        'real_estate': property,
        'cat_selected': 0,
    }
    return render(request, 'main/property_list.html', context=context)

# def property_list(request):
#     clients = Client.objects.all()
#
#     context = {
#         'title': 'Список недвижимости',
#         'menu': menu,
#         'clients': clients,
#         'cat_selected': 0,
#     }
#     return render(request, 'main/clients_list.html', context=context)



#CRUD