from django.urls import path, re_path
from  .views import *


urlpatterns = [
    path('', index, name='home'),
    path('property_list/', property_list, name='property_list'),
    path('property/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category')
]