from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Sport
from .serializers import SportsSerializer

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def listing_sports(request):

  sports = Sport.objects.all()
  serializer = SportsSerializer(sports, many=True)

  return JsonResponse({'data': serializer.data})