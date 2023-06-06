from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.contrib.auth.views import LoginView

menu = [{'title': 'Войти', 'url_name': 'login'},
        {'title': 'Добавить', 'url_name': 'add_page'},
        {'title': 'Клиенты', 'url_name': 'clients'},
        {'title': 'Сделки', 'url_name': 'deals'}]


class MainHome(DataMixin, ListView):
    model = RealEstate
    template_name = 'main/property_list.html'
    context_object_name = 'real_estate'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список недвижимости")

        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return RealEstate.objects.filter(purchased=False)


def index(request):
    return render(request, 'main/index.html')
# указывая html шаблон, представляем, что мы уже находимся в папке template


class PropertyCategory(DataMixin, ListView):
    model = RealEstate
    template_name = 'main/property_list.html'
    context_object_name = 'real_estate'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Список недвижимости определенной категории',
                                      cat_selected=context['real_estate'][0].type_id)

        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return RealEstate.objects.filter(type__id=self.kwargs['cat_id'], purchased=False)


# def addpage(request):
#     if request.method == 'POST':
#         form = AddDealForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddDealForm()
#     return render(request, 'main/addpage.html', {'form':form, 'menu': menu, 'title': "add"})

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddDealForm
    template_name = 'main/addpage.html'
    def get_context_data(self,*, object_list=None, **kwargs):
        context= super().get_context_data(**kwargs)
        c_def = self.get_user_context(title= 'Заключение сделки')
        return dict(list(context.items())+list(c_def.items()))


# class ClientsPage(LoginRequiredMixin, DataMixin, CreateView):
#     form_class = AddDealForm
#     template_name = 'main/index.html'
#     def get_context_data(self,*, object_list=None, **kwargs):
#         context= super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Клиенты')
#         return dict(list(context.items())+list(c_def.items()))
def clients(request):
    cl = Client.objects.all()

    context = {
        'title': 'Список клиентов',
        'menu': menu,
        'clients': cl,
        'cat_selected': 0,
    }
    return render(request, 'main/clients.html', context=context)

def deals(request):
    deals = Deal.objects.all()

    context = {
        'title': 'Список сделок',
        'menu': menu,
        'deals': deals,
        'cat_selected': 0,
    }
    return render(request, 'main/deals.html', context=context)

# class AddPage(DataMixin, ListView):
#     model = RealEstate
#     template_name = 'main/property_list.html'
#     context_object_name = 'real_estate'
#     allow_empty = False
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Список недвижимости определенной категории',
#                                       cat_selected=context['real_estate'][0].type_id)
#
#         return context

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name ='main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('property_list')

def logout_user(request):
    logout(request)
    return redirect('property_list')


def show_post(request, post_id):
    property = get_object_or_404(RealEstate, pk=post_id)

    context = {
        'property': property,
        'menu': menu,
        'title': property.title,
        'cat_selected': 1
    }
    return render(request, 'main/property.html', context=context)

# class ShowPost(DetailView):
#     model = RealEstate
#     template_name = 'main/property.html'
#     pk_url_kwarg = 'post_pk'

# def show_category(request, cat_id):
#     property = RealEstate.objects.filter(type_id=cat_id)
#
#
#     #if len(property) == 0:
#     #    raise Http404()
#
#     context = {
#         'title': 'Список недвижимости определенного типа',
#         'menu': menu,
#         'real_estate': property,
#         'cat_selected': cat_id,
#     }
#     return render(request, 'main/property_list.html', context=context)


# def property_list(request):
#     property = RealEstate.objects.all()
#
#     context = {
#         'title': 'Список недвижимости',
#         'menu': menu,
#         'real_estate': property,
#         'cat_selected': 0,
#     }
#     return render(request, 'main/property_list.html', context=context)



#CRUD