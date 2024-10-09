from rest_framework import serializers

from .models import Event, Sport

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class SportSerializer(serializers.ModelSerializer):

  class Meta:

    model = Sport
    fields = (
      'id_sport',
      'title',
      'url_image'
    )

# ____________________________________________________________________________________________________________________ #

class EventSerializer(serializers.ModelSerializer):

  # sport = serializers.CharField(source='sport.title')

  class Meta:

    model = Event
    fields = (
      'id_event',
      'sport',
      'date',
      'hours',
      'location',
      'price'
    )