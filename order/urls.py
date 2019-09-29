from django.conf.urls import url
from .views import get_restaurants, get_menu_items

urlpatterns = [
    url(r'^restaurants$', get_restaurants, name='restaurants$'),
    url(r'^menu-items$', get_menu_items, name='menu_items')
]