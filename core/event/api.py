from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Event, Sport
from .serializers import EventSerializer, SportSerializer

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_sports(request):

  sports = Sport.objects.all()
  serializer = SportSerializer(sports, many=True)

  return JsonResponse({'data': serializer.data})

# ------------------------------------------------------ #

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_events(request):

  events = Event.objects.all()

  sport = request.query_params.get("sport")

  if sport:
    events = events.filter(sport=sport)

  serializer = EventSerializer(events, many=True)

  return JsonResponse({'data': serializer.data})