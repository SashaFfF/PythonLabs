from .models import *

menu = [{'title': 'Войти', 'url_name': 'login'},
        {'title': 'Добавить', 'url_name': 'add_page'},
        {'title': 'Клиенты', 'url_name': 'clients'},
        {'title': 'Сделки', 'url_name': 'deals'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = PropertyType.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
            user_menu.pop(1)
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

