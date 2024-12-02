from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    version = models.CharField(max_length=50)
    date = models.DateField()

class MenuSection(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=255)
    order = models.IntegerField()

class MenuItem(models.Model):
    section = models.ForeignKey(MenuSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dietary_restriction_id = models.IntegerField()

class DietaryRestriction(models.Model):
    label = models.CharField(max_length=255)

class ProcessingLog(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    error_message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
