from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Duplicate)
admin.site.register(DuplicateType)

