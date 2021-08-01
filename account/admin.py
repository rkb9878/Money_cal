from django.contrib import admin
from .models import Account
# Register your models here.



@admin.register(Account)
class accountAdmin(admin.ModelAdmin):
    list_display = ['user','name','amount','is_personal','created', 'updated']
    list_filter = ['user__username','is_personal']
    search_fields = ['user__username']
