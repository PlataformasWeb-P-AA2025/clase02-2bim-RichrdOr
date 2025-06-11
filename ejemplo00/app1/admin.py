from django.contrib import admin

# Register your models here.

from app1.models import Estudiantes, Ciudad

admin.site.register(Estudiantes)

admin.site.register(Ciudad)