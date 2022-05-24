from django.contrib import admin
from .models import payment
# Register your models here.


@admin.register(payment)
class paymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')