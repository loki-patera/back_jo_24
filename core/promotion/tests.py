from django.test import TestCase

from .models import Offer

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class OfferTestCase(TestCase):

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