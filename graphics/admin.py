from django.contrib import admin
from .models import Category, Creature, Object, Landscape

admin.site.register(Category)
admin.site.register(Creature)
admin.site.register(Object)
admin.site.register(Landscape)
