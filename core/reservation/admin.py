from django.contrib import admin

from .models import Booking, Booking_Line

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

  list_display = ['booking_date', 'person']
  ordering = ['booking_date', 'person']

# -------------------------------------------------------------------------------------------------------------------- #

@admin.register(Booking_Line)
class BookingLineAdmin(admin.ModelAdmin):

  list_display = ['booking', 'event', 'offer', 'qrcode']