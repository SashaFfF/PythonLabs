from django.urls import path, re_path
from  .views import *


urlpatterns = [
    path('', index, name='home'),
    path('property_list/', MainHome.as_view(), name='property_list'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('property/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', PropertyCategory.as_view(), name='category')
]