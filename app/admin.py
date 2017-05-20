from django.contrib import admin

from .models import Country, Shop

class ShopInline(admin.TabularInline):
    model = Shop
    extra = 1

class CountryAdmin(admin.ModelAdmin):
    fieldsets = [
        ( None, {'fields': ['country_name']} ),
        ( 'Data', {'fields': ['pub_date']} ),
    ]
    inlines = [ShopInline]
    list_display = ('country_name', 'pub_date', 'was_published_recently')

admin.site.register(Country, CountryAdmin)
admin.site.register(Shop)