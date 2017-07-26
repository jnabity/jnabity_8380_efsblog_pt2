# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer




def home(request):
   return render(request, 'portfolio/home.html',
                 {'portfolio': home})


@login_required
def customer_list(request):
   customers = Customer.objects.filter(created_date__lte=timezone.now())
   return render(request, 'portfolio/customer_list.html', {'customers': customers})

@login_required
def customer_new(request):
   if request.method == "POST":
       form = CustomerForm(request.POST)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.created_date = timezone.now()
           customer.save()
           customers = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/customer_list.html',
                         {'customers': customers})
   else:
       form = CustomerForm()
       # print("Else")
   return render(request, 'portfolio/customer_new.html', {'form': form})

@login_required
def customer_edit(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.updated_date = timezone.now()
           customer.save()
           customers = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/customer_list.html',
                         {'customers': customers})
   else:
       # edit
       form = CustomerForm(instance=customer)
   return render(request, 'portfolio/customer_edit.html', {'form': form})


@login_required
def customer_delete(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   customer.delete()
   customers = Customer.objects.filter(created_date__lte=timezone.now())
   return render(request, 'portfolio/customer_list.html', {'customers': customers})


@login_required
def stock_list(request):
   stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
   return render(request, 'portfolio/stock_list.html', {'stocks': stocks})


@login_required
def stock_new(request):
   if request.method == "POST":
       form = StockForm(request.POST)
       if form.is_valid():
           stock = form.save(commit=False)
           stock.created_date = timezone.now()
           stock.save()
           stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/stock_list.html',
                         {'stocks': stocks})
   else:
       form = StockForm()
       # print("Else")
   return render(request, 'portfolio/stock_new.html', {'form': form})


@login_required
def stock_edit(request, pk):
   stock = get_object_or_404(Stock, pk=pk)
   if request.method == "POST":
       form = StockForm(request.POST, instance=stock)
       if form.is_valid():
           stock = form.save()
           # stock.customer = stock.id
           stock.updated_date = timezone.now()
           stock.save()
           stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/stock_list.html', {'stocks': stocks})
   else:
       # print("else")
       form = StockForm(instance=stock)
   return render(request, 'portfolio/stock_edit.html', {'form': form})


@login_required
def stock_delete(request, pk):
   stock = get_object_or_404(Stock, pk=pk)
   stock.delete()
   stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
   return render(request, 'portfolio/stock_list.html', {'stocks': stocks})


@login_required
def investment_list(request):
   investments = Investment.objects.filter(acquired_date__lte=timezone.now())
   return render(request, 'portfolio/investment_list.html', {'investments': investments})

@login_required
def investment_new(request):
   if request.method == "POST":
       form = InvestmentForm(request.POST)
       if form.is_valid():
           investment = form.save(commit=False)
           investment.created_date = timezone.now()
           investment.save()
           investments = Investment.objects.filter(acquired_date__lte=timezone.now())
           return render(request, 'portfolio/investment_list.html',
                         {'investments': investments})
   else:
       form = InvestmentForm()
       # print("Else")
   return render(request, 'portfolio/investment_new.html', {'form': form})

@login_required
def investment_edit(request, pk):
   investment = get_object_or_404(Investment, pk=pk)
   if request.method == "POST":
       form = InvestmentForm(request.POST, instance=investment)
       if form.is_valid():
           investment = form.save()
           # stock.customer = stock.id
           investment.updated_date = timezone.now()
           investment.save()
           investments = Investment.objects.filter(acquired_date__lte=timezone.now())
           return render(request, 'portfolio/investment_list.html', {'investments': investments})
   else:
       # print("else")
       form = InvestmentForm(instance=investment)
   return render(request, 'portfolio/investment_edit.html', {'form': form})

@login_required
def investment_delete(request, pk):
    investment = get_object_or_404(Investment, pk=pk)
    investment.delete()
    investments = Investment.objects.filter(acquired_date__lte=timezone.now())
    return render(request, 'portfolio/investment_list.html', {'investments': investments})

@login_required
def mutual_list(request):
   mutuals = MutualFund.objects.filter(purchase_date__lte=timezone.now())
   return render(request, 'portfolio/mutual_list.html', {'mutuals': mutuals})


@login_required
def mutual_new(request):
   if request.method == "POST":
       form = MutualForm(request.POST)
       if form.is_valid():
           mutual = form.save(commit=False)
           mutual.created_date = timezone.now()
           mutual.save()
           mutuals = MutualFund.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/mutual_list.html',
                         {'mutuals': mutuals})
   else:
       form = MutualForm()
       # print("Else")
   return render(request, 'portfolio/mutual_new.html', {'form': form})


@login_required
def mutual_edit(request, pk):
   mutual = get_object_or_404(MutualFund, pk=pk)
   if request.method == "POST":
       form = MutualForm(request.POST, instance=mutual)
       if form.is_valid():
           mutual = form.save()
           mutual.updated_date = timezone.now()
           mutual.save()
           mutuals = MutualFund.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/mutual_list.html', {'mutuals': mutuals})
   else:
       form = MutualForm(instance=mutual)
   return render(request, 'portfolio/mutual_edit.html', {'form': form})


@login_required
def mutual_delete(request, pk):
   mutual = get_object_or_404(MutualFund, pk=pk)
   mutual.delete()
   mutuals = MutualFund.objects.filter(purchase_date__lte=timezone.now())
   return render(request, 'portfolio/mutual_list.html', {'mutuals': mutuals})



@login_required
def portfolio(request,pk):
   customer = get_object_or_404(Customer, pk=pk)
   customers = Customer.objects.filter(created_date__lte=timezone.now())
   investments =Investment.objects.filter(customer=pk).filter(acquired_date__lte=timezone.now())
   stocks = Stock.objects.filter(customer=pk).filter(purchase_date__lte=timezone.now())
   sum_acquired_value = Investment.objects.filter(customer=pk).aggregate(Sum('acquired_value'))
   sum_recent_value = Investment.objects.filter(customer=pk).aggregate(Sum('recent_value'))
   mutuals = MutualFund.objects.filter(customer=pk).filter(purchase_date__lte=timezone.now())
   sum_mutual_purchase_value = MutualFund.objects.filter(customer=pk).aggregate(Sum('purchase_net_asset_value'))
   sum_mutual_recent_value = MutualFund.objects.filter(customer=pk).aggregate(Sum('recent_net_asset_value'))


   return render(request, 'portfolio/portfolio.html', {'customers': customers, 'investments': investments,
                                                      'stocks': stocks,
                                                      'sum_acquired_value': sum_acquired_value,
                                                       'sum_recent_value': sum_recent_value,
                                                       'mutuals': mutuals,
                                                       'sum_mutual_purchase_value': sum_mutual_purchase_value,
                                                       'sum_mutual_recent_value': sum_mutual_recent_value,
                                                       })


# List at the end of the views.py
# Lists all customers
class CustomerList(APIView):

    def get(self,request):
        customers_json = Customer.objects.all()
        serializer = CustomerSerializer(customers_json, many=True)
        return Response(serializer.data)
