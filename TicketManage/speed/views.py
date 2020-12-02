from random import random

from django.contrib.auth.handlers.modwsgi import check_password
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
import time

from speed.models import someTips, tickets, customer


def index(request):
    allTips = someTips.objects.all()
    news = someTips.objects.filter(group="new")
    problem = someTips.objects.filter(group="problem")
    travelTips = someTips.objects.filter(group="travelTips")
    allTickets = tickets.objects.all()
    inticket = tickets.objects.filter(type="in")
    outticket = tickets.objects.filter(type='out')
    contex = {
        'allTips': allTips,
        'news': news,
        'problem': problem,
        'travelTips': travelTips,
        'allTickets': allTickets,
        'inticket': inticket,
        'outticket': outticket,

    }
    return render(request, 'speed/index.html', contex)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('name')
        password = request.POST.get('password')

        if email == customer.objects.filter(u_email=email).exists():
            user = customer.objects.get(u_email=email)
            if check_password(password, user.u_password):
                ticket = ''
                for i in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    ticket += random.choice(5)
                now_time = int(time.time())
                ticket = "TK" + ticket + str(now_time)
                response = HttpResponseRedirect(index)
                response.set_cookie('ticket', ticket, max_age=10000)
                user.u_ticket = ticket
                user.save()
                return response
            else:
                return render(request, "user/in.html", {'password': "用户密码错误"})

        else:
            return render(request, "user/in.html", {'user': "用户不存在"})

    contex = {

    }
    return render(request, 'user/in.html', contex)


def register(request):
    if request.method == 'POST' and request.POST.get("name") != "":
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        password = make_password(password)
        customer.objects.create(u_name=name, u_password=password, u_email=email)

    context = {

    }
    return render(request, 'user/register.html', context)
