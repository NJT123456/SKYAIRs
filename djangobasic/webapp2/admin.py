from typing import Reversible
from django.contrib import admin
from django.urls import reverse
from .models import *
from django.utils.http import urlencode

# Register your models here.

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['code','city','airport','city_thai','airport_thai','country']

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['fid','fnumber','origin','destination','depart_date','airline','seat_class']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['ref_no','flight','flight_departdate','seat_class','status']


class PassengerInLineAdmin(admin.TabularInline):
    model = Passenger

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','phone','is_staff']
    inlines = [PassengerInLineAdmin]

admin.site.register(User, UserAdmin)

        