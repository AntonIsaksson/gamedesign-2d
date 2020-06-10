from django.contrib import admin
from .models import Category, CreatureFree, CreaturePremium, ObjectFree, ObjectPremium, LandscapeFree, LandscapePremium

admin.site.register(Category)
admin.site.register(CreatureFree)
admin.site.register(CreaturePremium)
admin.site.register(ObjectFree)
admin.site.register(ObjectPremium)
admin.site.register(LandscapeFree)
admin.site.register(LandscapePremium)
