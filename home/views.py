from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db import transaction
# Create your views here.
def home(request):
    if request.method == 'POST':
        try:
            user_one = request.POST.get('user_one')
            user_two = request.POST.get('user_two')
            amount = int(request.POST.get('amount'))
            with transaction.atomic():
                user_one_payment_obj = payment.objects.get(user=user_one)
                user_two_payment_obj = payment.objects.get(user=user_two)
                
                user_one_payment_obj.amount -= amount
                user_one_payment_obj.save()
                
                user_two_payment_obj.amount += amount
                user_two_payment_obj.save()
            
            messages.success(request, 'Payment Successful')
        except Exception as e:
            print(e)
            messages.success(request, 'Payment Failed')
            
    return render(request, 'index.html')