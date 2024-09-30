from datetime import datetime
from django.test import TestCase

from .models import Competition, Event, Sport
from .utils import time_zone

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class SportTestCase(TestCase):

  def test_sport_create(self) -> None:

    """ Teste si une épreuve sportive a été ajoutée en base de données """

    number_sports_initial = Sport.objects.count()

    new_sport = Sport()
    new_sport.title = "Cyclisme sur piste"
    new_sport.image = "images/sports/cyclisme-sur-piste.jpg"
    new_sport.save()

    number_sports_final = Sport.objects.count()

    self.assertTrue(number_sports_final == number_sports_initial + 1)

# -------------------------------------------------------------------------------------------------------------------- #

class EventTestCase(TestCase):

  def setUp(self) -> None:
    
    """ Initialise des données fictives """

    self.element_sport = Sport()
    self.element_sport.title = "Cyclisme sur piste"
    self.element_sport.image = "images/sports/cyclisme-sur-piste.jpg"
    self.element_sport.save()
  

  def test_event_create(self) -> None:

    """ Teste si un évènement a été ajouté en base de données """

    number_events_initial = Event.objects.count()

    new_event = Event()
    new_event.sport = self.element_sport
    new_event.location = "Vélodrome National | SAINT-QUENTIN-EN-YVELINES"
    new_event.start_date = time_zone(datetime(2024, 8, 5, 17, 0))
    new_event.end_date = time_zone(datetime(2024, 8, 5, 20, 0))
    new_event.price = 50.00
    new_event.save()

    number_events_final = Event.objects.count()

    self.assertTrue(number_events_final == number_events_initial + 1)

# -------------------------------------------------------------------------------------------------------------------- #

class CompetitionTestCase(TestCase):

  def setUp(self) -> None:
    
    """ Initialise des données fictives """

    self.element_sport = Sport()
    self.element_sport.title = "Cyclisme sur piste"
    self.element_sport.image = "images/sports/cyclisme-sur-piste.jpg"
    self.element_sport.save()

    self.element_event = Event()
    self.element_event.sport = self.element_sport
    self.element_event.location = "Vélodrome National | SAINT-QUENTIN-EN-YVELINES"
    self.element_event.start_date = time_zone(datetime(2024, 8, 5, 17, 0))
    self.element_event.end_date = time_zone(datetime(2024, 8, 5, 20, 0))
    self.element_event.price = 50.00
    self.element_event.save()


  def test_competition_create(self) -> None:

    """ Teste si une compétition a été ajoutée en base de données """

    number_competitions_initial = Competition.objects.count()

    new_competition = Competition()
    new_competition.description = "Vitesse par équipe"
    new_competition.gender = "Femme"
    new_competition.phase = "Qualifications"
    new_competition.event = self.element_event
    new_competition.save()

    number_competitions_final = Event.objects.count()

    self.assertTrue(number_competitions_final == number_competitions_initial + 1)