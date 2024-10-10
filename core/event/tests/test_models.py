from datetime import datetime
from django.test import TestCase

from event.models import Competition, Event, Sport
from event.utils import time_zone

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class SportTestCase(TestCase):

  def setUp(self) -> None:

    """ Initialise des données fictives """

    self.element_sport = Sport()
    self.element_sport.title = "Golf"
    self.element_sport.image = "images/sports/gaffe.jpg"
    self.element_sport.save()
  
  # ------------------------------------------------------ #

  def test_str_sport(self) -> None:

    """ Teste si la méthode __str__ de la classe Sport retourne la valeur correcte """

    self.assertTrue(Sport.__str__(self.element_sport) == "Golf")
  
  # ------------------------------------------------------ #

  def test_sport_create(self) -> None:

    """ Teste si une épreuve sportive a été ajoutée en base de données """

    number_sports_initial = Sport.objects.count()

    new_sport = Sport()
    new_sport.title = "Cyclisme sur piste"
    new_sport.image = "images/sports/cyclisme-sur-piste.jpg"
    new_sport.save()

    number_sports_final = Sport.objects.count()

    self.assertTrue(number_sports_final == number_sports_initial + 1)
  
  # ------------------------------------------------------ #

  def test_sport_update(self) -> None:

    """ Teste si une épreuve sportive a été modifiée en base de données """

    self.assertEqual(self.element_sport.title, 'Golf')

    self.element_sport.image = "images/sports/golf.jpg"
    self.element_sport.save()

    temp_sport = Sport.objects.get(pk=self.element_sport.id_sport)

    self.assertEqual(temp_sport.image, "images/sports/golf.jpg")
  
  # ------------------------------------------------------ #

  def test_sport_delete(self) -> None:

    """ Teste si une épreuve sportive a été supprimée en base de données """

    number_sports_initial = Sport.objects.count()

    self.element_sport.delete()

    number_sports_final = Sport.objects.count()

    self.assertTrue(number_sports_final == number_sports_initial - 1)

# ____________________________________________________________________________________________________________________ #

class EventTestCase(TestCase):

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
    self.element_event.end_date = time_zone(datetime(2024, 8, 5, 23, 30))
    self.element_event.price = 50.00
    self.element_event.save()
  
  # ------------------------------------------------------ #

  def test_str_event(self) -> None:

    """ Teste si la méthode __str__ de la classe Event retourne la valeur correcte """
    
    self.assertEqual(Event.__str__(self.element_event), "Cyclisme sur piste | 05/08/2024 (17:00 - 23:30)")
  
  # ------------------------------------------------------ #

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
  
  # ------------------------------------------------------ #
  
  def test_event_update(self) -> None:

    """ Teste si un évènement a été modifié en base de données """

    self.assertEqual(self.element_event.sport, self.element_sport)
    self.assertEqual(self.element_event.location, "Vélodrome National | SAINT-QUENTIN-EN-YVELINES")
    self.assertEqual(self.element_event.start_date, time_zone(datetime(2024, 8, 5, 17 ,0)))

    self.element_event.end_date = time_zone(datetime(2024, 8, 5, 20, 0))
    self.element_event.save()

    temp_event = Event.objects.get(pk=self.element_event.id_event)

    self.assertEqual(temp_event.end_date, time_zone(datetime(2024, 8, 5, 20, 0)))
  
  # ------------------------------------------------------ #

  def test_event_delete(self) -> None:

    """ Teste si un évènement a été supprimé en base de données """

    number_events_initial = Event.objects.count()

    self.element_event.delete()

    number_events_final = Event.objects.count()

    self.assertTrue(number_events_final == number_events_initial - 1)

# ____________________________________________________________________________________________________________________ #

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

    self.element_competition = Competition()
    self.element_competition.description = "Vitesse par équipe"
    self.element_competition.gender = "Homme"
    self.element_competition.phase = "1er Tour"
    self.element_competition.event = self.element_event
    self.element_competition.save()
  
    # ------------------------------------------------------ #

  def test_str_competition(self) -> None:

    """ Teste si la méthode __str__ de la classe Competition retourne la valeur correcte """

    self.assertEqual(
      Competition.__str__(self.element_competition),
      "Cyclisme sur piste | 05/08/2024 (17:00 - 20:00) | Homme, Vitesse par équipe, 1er Tour"
    )

  # ------------------------------------------------------ #

  def test_competition_create(self) -> None:

    """ Teste si une compétition a été ajoutée en base de données """

    number_competitions_initial = Competition.objects.count()

    new_competition = Competition()
    new_competition.description = "Vitesse par équipe"
    new_competition.gender = "Femme"
    new_competition.phase = "Qualifications"
    new_competition.event = self.element_event
    new_competition.save()

    number_competitions_final = Competition.objects.count()

    self.assertTrue(number_competitions_final == number_competitions_initial + 1)
  
  # ------------------------------------------------------ #

  def test_competition_update(self) -> None:

    """ Teste si une compétition a été modifié en base de données """

    self.assertEqual(self.element_competition.description, "Vitesse par équipe")
    self.assertEqual(self.element_competition.phase, "1er Tour")
    self.assertEqual(self.element_competition.event, self.element_event)

    self.element_competition.gender = "Femme"
    self.element_competition.save()

    temp_competition = Competition.objects.get(pk=self.element_competition.id_competition)

    self.assertEqual(temp_competition.gender, "Femme")
  
  # ------------------------------------------------------ #

  def test_competition_delete(self) -> None:

    """ Teste si une compétition a été supprimée en base de données """

    number_competitions_initial = Competition.objects.count()

    self.element_competition.delete()

    number_competitions_final = Competition.objects.count()

    self.assertTrue(number_competitions_final == number_competitions_initial - 1)