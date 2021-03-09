from django.contrib import admin

# Register your models here.
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user_name','sexe','address', 'phone','city','country','zipcode','image_tag']

admin.site.register(Customer,CustomerAdmin)