from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, ListView
from . import models, forms
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def elems_view(request):
    elems_1 = models.Elems_1.objects.all()
    elems_2 = models.Elems_2.objects.all()
    elems_3 = models.Elems_3.objects.all()
    elems_4 = models.Elems_4.objects.all()
    context = {
        'elems_1': elems_1,
        'elems_2': elems_2,
        'elems_3': elems_3,
        'elems_4': elems_4
    }
    return render(request, 'main_page.html', context)

def elems_1_detail_view(request, id):
    elems_1 = get_object_or_404(models.Elems_1, id=id)
    return render(request, 'elems_1_detail.html', {'elems_1': elems_1})

def elems_2_detail_view(request, id):
    elems_2 = get_object_or_404(models.Elems_2, id=id)
    return render(request, 'elems_2_detail.html', {'elems_2': elems_2})

def elems_3_detail_view(request, id):
    elems_3 = get_object_or_404(models.Elems_3, id=id)
    return render(request, 'elems_3_detail.html', {'elems_3': elems_3})

def elems_4_detail_view(request, id):
    elems_4 = get_object_or_404(models.Elems_4, id=id)
    return render(request, 'elems_4_detail.html', {'elems_4': elems_4})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})

def order_view(request):
    order = models.Order.objects.all()
    return render(request, 'order.html', {'order': order})

def add_order_view(request):
    method = request.method
    if method == 'POST':
        form = forms.Order_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<center style="font-size:50px;display: block;'
                                'height:100vh; display:flex; justify-content:center; align-items:center; '
                                'width:100%;background-image: url('
                                '../static/images/aesthetic-background-with-abstract-neon-led-light-effect.jpg); '
                                'background-size: cover;margin:0;box-sizing: border-box;padding: 0; object-fit: contain;'
                                'color: white;'
                                '"><b>Your order is '
                                'accepted!</a></b>'
                                '<br></br>'
                                '<center><p><a href="/main_page/" style="text-decoration:none; color:white; '
                                'font-size:30px">Click to '
                                'go to the main page</p></center></center>')
    else:
        form = forms.Order_form()

    return render(request, 'add_order.html', {'form': form})

def about_us_view(request):
    about_us = models.About_us.objects.all()
    return render(request, 'about_us.html', {'about_us': about_us})