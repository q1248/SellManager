import random

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
import time

from speed.models import someTips, tickets, customer, PurchaseHistory


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
    ticket = request.COOKIES.get('ticket')
    if customer.objects.filter(u_ticket=ticket).exists():
        cusinfo = customer.objects.get(u_ticket=ticket)
        contex.update({"cusinfo": cusinfo})
        return render(request, 'speed/welcome.html', contex)

    return render(request, 'speed/index.html', contex)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if customer.objects.filter(u_email=email).exists():
            user = customer.objects.get(u_email=email)
            if check_password(password, user.u_password):
                ticket = ''
                for i in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = "TK" + ticket + str(now_time)
                response = HttpResponseRedirect('/')
                response.set_cookie('ticket', ticket, max_age=10000)
                user.u_ticket = ticket
                user.save()

                return response
            else:
                return render(request, 'user/in.html', {"message": "密码错误!"})
        else:
            return render(request, 'user/in.html', {"message": "用户不存在!"})

        redirect('index')

    return render(request, 'user/in.html')


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


def space(request):
    global u_logs

    ticket = request.COOKIES.get('ticket')
    if not ticket:
        return HttpResponseRedirect('/login/')

        # 主要是得到了cookie后进行的操作
    user = customer.objects.get(u_ticket=ticket)
    if PurchaseHistory.objects.filter(customerName=user.id).exists():
        own = PurchaseHistory.objects.filter(customerName=user.id)
        u_logs = []

        for i in own:
            if tickets.objects.filter(id=i.ticketId).exists():
                w = tickets.objects.filter(id=i.ticketId)
                for s in w:
                    u_logs.append(s)
            else:
                break
        print(u_logs)
        return render(request, "user/space.html", {"u_logs": u_logs})
    else:
        return render(request, 'user/spacex.html')


def logout(request):
    if request.method == "GET":
        reponse = HttpResponseRedirect('/login')
        reponse.delete_cookie('ticket')
        return reponse


def myprofile(request):
    if is_login(request):
        ticket = request.COOKIES.get('ticket')
        cusinfo = customer.objects.get(u_ticket=ticket)
        context = {
            "cusinfo": cusinfo,
        }
        return render(request, 'user/usrprofile.html', context)
    else:
        reponse = HttpResponseRedirect('/login')
        return reponse


def is_login(request):
    ticket = request.COOKIES.get('ticket')
    if customer.objects.filter(u_ticket=ticket).exists():
        return True
    else:
        return False


def buy(request, PK):
    # 购买成功,剩余票数减少

    if PurchaseHistory.objects.filter(ticketId=PK).exists():
        reponse = HttpResponseRedirect("/")
        return reponse
    tk = tickets.objects.get(id=PK)
    tk.leftTicket -= 1
    tk.save()
    # 在购买记录中添加记录购买者的id和票的id
    ticket = request.COOKIES.get('ticket')
    user = customer.objects.get(u_ticket=ticket)
    PurchaseHistory.objects.create(customerName=user.id, ticketId=PK)

    return render(request, 'speed/buy.html')


def remove(request, PK):
    tk = tickets.objects.get(id=PK)
    tk.leftTicket += 1
    tk.save()
    PurchaseHistory.objects.get(ticketId=PK).delete()
    return render(request, 'speed/remove.html')


def news(request, PK):
    news = someTips.objects.get(id=PK)

    return render(request, 'article/news.html', {'news': news})


def privage(request):
    return render(request, 'user/privage.html')
