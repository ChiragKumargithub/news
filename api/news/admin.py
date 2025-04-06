from django.contrib import admin
from .models import news ,register

# Register your models here.

admin.site.register(news)

class register_admin(admin.ModelAdmin):
    list_display=["id","username","email","mobile"]

admin.site.register(register,register_admin)    


