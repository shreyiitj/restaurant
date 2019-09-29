from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from .models import Restaurants, RestaurantMenuItem


def get_restaurants(request):
    data = Restaurants.objects.all()[:10]
    response = {'restaurants': []}
    for entry in data:
        response['restaurants'].append(
            {'id': entry.id, 'name': entry.name, 'address': entry.address})

    return render(request, 'order/restaurant.html', response)


def get_menu_items(request):
    res_id = request.GET.get('res_id')
    res_details = Restaurants.objects.filter(id=res_id)[0]
    items = list(RestaurantMenuItem.objects.filter(res=res_id).values())
    return render(request, 'order/items.html', {'items': items, 'res_name': res_details.name})
