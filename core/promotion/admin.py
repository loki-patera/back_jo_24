from django.contrib import admin

from .models import Offer

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):

  list_display = ['type', 'number_seats', 'discount']
  ordering = ['number_seats', 'discount']