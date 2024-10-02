from django.test import TestCase

from .models import Offer

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class OfferTestCase(TestCase):

  def setUp(self) -> None:
    
    """ Initialise des données fictives """

    self.element_offer = Offer()
    self.element_offer.type = "Groupe - 4 adultes / 1 enfant"
    self.element_offer.number_seats = 5
    self.element_offer.discount = 13
    self.element_offer.save()
  
  # ------------------------------------------------------ #

  def test_str_offer(self) -> None:

    """ Teste si la méthode __str__ de la classe Offer retourne la valeur correcte """

    self.assertTrue(Offer.__str__(self.element_offer) == "Groupe - 4 adultes / 1 enfant")

  # ------------------------------------------------------ #

  def test_offer_create(self) -> None:

    """ Teste si une offre a été ajoutée en base de données """

    number_offers_initial = Offer.objects.count()

    new_offer = Offer()
    new_offer.type = "Groupe - 5 adultes / 2 enfants"
    new_offer.number_seats = 7
    new_offer.discount = 19
    new_offer.save()

    number_offers_final = Offer.objects.count()

    self.assertTrue(number_offers_final == number_offers_initial + 1)
  
  # ------------------------------------------------------ #

  def test_offer_update(self) -> None:

    """ Teste si une offre a été modifiée en base de données """

    self.assertEqual(self.element_offer.type, "Groupe - 4 adultes / 1 enfant")

    self.element_offer.discount = 14
    self.element_offer.save()

    temp_offer = Offer.objects.get(pk=self.element_offer.id_offer)

    self.assertEqual(temp_offer.discount, 14)
  
  # ------------------------------------------------------ #

  def test_offer_delete(self) -> None:

    """ Teste si une offre a été supprimée en base de données """

    number_offers_initial = Offer.objects.count()

    self.element_offer.delete()

    number_offers_final = Offer.objects.count()

    self.assertTrue(number_offers_final == number_offers_initial - 1)