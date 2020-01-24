from django.contrib import admin

# Register your models here.
from .models import Account_detail, Account_User_ID

admin.site.register(Account_detail)
admin.site.register(Account_User_ID)
