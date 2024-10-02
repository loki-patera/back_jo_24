from datetime import datetime

from django.test import TestCase

from .admin import PersonAdmin

from .models import Person

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class PersonTestCase(TestCase):

  def setUp(self) -> None:

    """ Initialise des données fictives """

    self.element_person = Person()
    self.element_person.firstname = "John"
    self.element_person.lastname = "Doe"
    self.element_person.date_of_birth = datetime(1987, 4, 19)
    self.element_person.country = "Belgique"
    self.element_person.save()

    self.element_person_2 = Person()
    self.element_person_2.firstname = "Michaël"
    self.element_person_2.lastname = "Kemaur"
    self.element_person_2.date_of_birth = datetime(2012, 9, 12)
    self.element_person_2.country = "France"
    self.element_person_2.save()
  
  # ------------------------------------------------------ #
  
  def test_str_person(self) -> None:

    """ Teste si la méthode __str__ de la classe Person retourne la valeur correcte """

    self.assertEqual(Person.__str__(self.element_person), "Doe John")
  
  # ------------------------------------------------------ #

  def test_status_is_adult(self) -> None:

    """ Teste si la méthode status de la classe PersonAdmin retourne 'Adulte' """
    
    self.assertEqual(PersonAdmin.status(self, self.element_person), "Adulte")
  
  # ------------------------------------------------------ #

  def test_status_is_child(self) -> None:

    """ Teste si la méthode status de la classe PersonAdmin retourne 'Enfant' """
    
    self.assertEqual(PersonAdmin.status(self, self.element_person_2), "Enfant")