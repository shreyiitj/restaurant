from django.db import models


class Restaurants(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)


class RestaurantMenuItem(models.Model):
    res = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=20)
    item_cost = models.FloatField(max_length=20)


# class Order(models.Model):
#     res = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
#     details = Json()
