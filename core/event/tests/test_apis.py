from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from event.serializers import EventSerializer, SportSerializer
from event.models import Event, Sport
from event.utils import time_zone

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class ListSportsTest(TestCase):

  def setUp(self) -> None:

    """ Initialise des données fictives """

    self.client = APIClient()

    self.sport1 = Sport.objects.create(
      title='Escalade',
      image='images/sports/escalade.jpg'
    )
    self.sport2 = Sport.objects.create(
      title='Surf',
      image='images/sports/surf.jpg'
    )
  
  # ------------------------------------------------------ #

  def test_list_sports(self) -> None:

    """ Teste si les données retournées sont correctes """

    response = self.client.get(reverse('sports'))

    sports = Sport.objects.all()
    serializer = SportSerializer(sports, many=True)

    self.assertEqual(response.json()['data'], serializer.data)

# ____________________________________________________________________________________________________________________ #

class ListEventsTest(TestCase):

  def setUp(self) -> None:

    """ Initialise des données fictives """

    self.client = APIClient()

    self.sport = Sport.objects.create(
      title='Escalade',
      image='images/sports/escalade.jpg'
    )
    self.event = Event.objects.create(
      sport=self.sport,
      location="Site d'escalade du Bourget",
      start_date= time_zone(datetime(2024, 8, 7, 10, 0)),
      end_date= time_zone(datetime(2024, 8, 7, 13, 0)),
      price=75.00
    )
  
  # ------------------------------------------------------ #

  def test_list_events(self) -> None:

    """ Teste si le statut de la réponse est 200 OK """

    response = self.client.get(reverse('events'))

    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  # ------------------------------------------------------ #

  def test_list_events_filtered_by_sport(self) -> None:

    """ Teste si les données filtrées sont correctes """

    response = self.client.get(reverse('events'), {'sport': self.sport.id_sport})

    events = Event.objects.filter(sport=self.sport)
    serializer = EventSerializer(events, many=True)

    self.assertEqual(response.json()['data'], serializer.data)