from django.contrib import admin

# Register your models here.
from .models import Categories,Host,Properties,Places

admin.site.register(Categories)
admin.site.register(Host)
admin.site.register(Properties)
admin.site.register(Places)