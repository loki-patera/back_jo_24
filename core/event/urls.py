from django.urls import path

from . import api

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

urlpatterns = [
  path('sports', api.list_sports, name="sports"),
  path('events', api.list_events, name="events")
]