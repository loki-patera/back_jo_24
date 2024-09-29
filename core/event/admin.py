from django.contrib import admin
from django.db import models
from django.utils.html import format_html

from .models import Event, Sport
from .utils import ImageWidget

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):

  formfield_overrides = {
    models.ImageField: {"widget": ImageWidget}
  }

  def image_tag(self, obj):

    """ Retourne une vignette de l'image """
  
    return format_html(
      f'''<a href="{obj.image.url}" target="_blank">
            <img src="{obj.image.url}" alt="{obj.title}" width="80"/>
          </a>'''
      )

  image_tag.short_description = 'Vignette'

  
  list_display = ['title', 'image_tag']

# -------------------------------------------------------------------------------------------------------------------- #

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

  list_display = ['sport', 'location', 'start_date', 'end_date']