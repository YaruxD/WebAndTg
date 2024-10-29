from django.contrib import admin
from WebAndTg.models import Catalog
from telegramapp.models import TelegramSales, TelegramUsers

admin.site.register(Catalog)
admin.site.register(TelegramSales)
admin.site.register(TelegramUsers)
# Register your models here.
