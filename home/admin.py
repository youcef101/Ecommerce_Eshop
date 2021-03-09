from django.contrib import admin
from .models import *
# Register your models here.
class SettingtAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer','ordernumber','status']
    list_filter = ['status']


admin.site.register(FAQ,FAQAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Setting,SettingtAdmin)