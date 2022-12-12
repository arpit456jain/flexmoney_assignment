from django.contrib import admin

# Register your models here.
from .models import Application_form, Alredy_registered_user


admin.site.register(Application_form)
admin.site.register(Alredy_registered_user)