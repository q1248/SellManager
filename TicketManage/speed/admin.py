from django.contrib import admin
from speed import models

# Register your models here.
from speed.models import someTips, tickets, customer, PurchaseHistory

admin.site.register(someTips)
admin.site.register(tickets)
admin.site.register(customer)
admin.site.register(PurchaseHistory)
