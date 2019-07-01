from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
import django.contrib.auth.admin
from . import views
from .models import Employee, Picture, TempPhoto, Token


admin.autodiscover()

# Unregister default models
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(Token)
# Register create models
admin.site.register(Employee)
admin.site.register(Picture)
admin.site.register(TempPhoto)
