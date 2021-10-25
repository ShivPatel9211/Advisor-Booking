from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Advisor ,Booking
user=get_user_model()
admin.site.register(Advisor)
admin.site.register(user)
admin.site.register(Booking)
# Register your models here.
