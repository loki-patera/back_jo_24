import pytz

from datetime import datetime

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class ImageWidget(AdminFileWidget):

  """ Classe pour retourner une vignette """
  
  def render(self, name, value, attrs=None, renderer=None):

    result = []

    if hasattr(value, "url"):
      result.append(
        f'''<a href="{value.url}" target="_blank" style="margin:5px">
              <img 
                src="{value.url}" alt="{value}" 
                width="200"
              />
            </a>'''
      )
    
    result.append(super().render(name, value, attrs, renderer))

    return format_html("".join(result))

# -------------------------------------------------------------------------------------------------------------------- #

def time_zone(date: datetime) -> datetime:

  """ Retourne la date au fuseau horaire de Paris """

  tz_Paris = pytz.timezone('Europe/Paris')
  return date.astimezone(tz_Paris)