from rest_framework import serializers

from .models import Sport

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class SportsSerializer(serializers.ModelSerializer):

  class Meta:

    model = Sport
    fields = (
      'id_sport',
      'title',
      'url_image'
    )