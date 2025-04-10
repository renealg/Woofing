from django.contrib import admin
from .models import DogBoarding

# Register your models here.


class BoardingAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'price_per_night', 'image', 'approved')
    list_filter = ('approved',)


admin.site.register(DogBoarding, BoardingAdmin)
