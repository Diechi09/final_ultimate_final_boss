from django.contrib import admin
from .models import Restaurant, Menu, MenuSection, MenuItem, DietaryRestriction, ProcessingLog

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')  # Fields to display in the admin list view
    search_fields = ('name', 'location')       # Enable search by name and location

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'version', 'date')
    list_filter = ('date',)                   # Filter menus by date
    search_fields = ('version',)              # Enable search by version

@admin.register(MenuSection)
class MenuSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu', 'section_name', 'order')
    list_filter = ('menu',)                   # Filter by related menu
    ordering = ('order',)                     # Order by the 'order' field

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'name', 'price', 'dietary_restriction_id')
    search_fields = ('name',)                 # Enable search by name
    list_filter = ('section', 'dietary_restriction_id')

@admin.register(DietaryRestriction)
class DietaryRestrictionAdmin(admin.ModelAdmin):
    list_display = ('id', 'label')
    search_fields = ('label',)                # Enable search by label

@admin.register(ProcessingLog)
class ProcessingLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu', 'status', 'timestamp')
    list_filter = ('status', 'timestamp')     # Filter logs by status and timestamp
