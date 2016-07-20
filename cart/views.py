# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Product
from .forms import ProductForm


def calculate_total(request):
    # Check if we have some data in our request GET dictionary
    if request.GET:
        # Initializing form with request data
        form = ProductForm(request.GET)
        if form.is_valid():
            # Retrieve data from form and session objects
            # If session object is empty, update it with request data
            product = form.cleaned_data['title']
            data = request.session.get('data', [])
            data.append(product)
            request.session['data'] = data

            # Get prices and special_prices for all products from DB
            a_price = Product.objects.get(title='A').price
            a_special_price = Product.objects.get(title='A').special_price
            b_price = Product.objects.get(title='B').price
            b_special_price = Product.objects.get(title='B').special_price
            c_price = Product.objects.get(title='C').price
            d_price = Product.objects.get(title='D').price
            e_price = Product.objects.get(title='E').price

            # Get products from current session by theirs name, exept for 'C'
            a_qty = data.count('A')
            b_qty = data.count('B')
            d_qty = data.count('D')
            e_qty = data.count('E')

            # Calculate total price for A product
            regular_price = a_price
            special_price = a_special_price
            remainder = a_qty % 3
            a_total = 0

            if remainder == 0:
                a_total = (a_qty / 3) * special_price
            else:
                sub_total = a_qty - remainder
                sub_total = (sub_total / 3) * special_price
                remainder = remainder * regular_price
                a_total = sub_total + remainder

            # Calculate total price for B product
            regular_price = b_price
            special_price = b_special_price
            remainder = b_qty % 2
            b_total = 0

            if remainder == 0:
                b_total = (b_qty / 2) * special_price
            else:
                sub_total = b_qty - remainder
                sub_total = (sub_total / 2) * special_price
                remainder = remainder * regular_price
                b_total = sub_total + remainder

            # Calculate total price for C product
            try:
                kgs = int(request.GET.get('kgs', 0))
            except ValueError:
                kgs = 0
            kgs_qty = int(request.session.get('kgs_qty', 0))
            total_kgs = kgs + kgs_qty
            request.session['kgs_qty'] = total_kgs
            c_total = c_price * total_kgs

            # Calculate total price for D product
            d_total = d_qty * d_price

            # Calculate total price for E product
            e_free = (d_qty // 2)  # Free E product for each two D products
            e_total = e_qty * e_price
            e_qty += e_free

            # Total price for all products we have in the cart
            total_price = (a_total + b_total + c_total + d_total + e_total)

            context = {
                    'form': form,
                    'a_total': a_total,
                    'b_total': b_total,
                    'c_total': c_total,
                    'd_total': d_total,
                    'e_total': e_total,
                    'a_qty': a_qty,
                    'b_qty': b_qty,
                    'd_qty': d_qty,
                    'e_qty': e_qty,
                    'total_kgs': total_kgs,
                    'total_price': total_price}

    else:
        # If our request.GET dictionary is empty, we clear all session data
        request.session['data'] = []
        request.session['kgs_qty'] = 0
        form = ProductForm()
        context = {'form': form}

    return render(request, 'cart/cart.html', context)
