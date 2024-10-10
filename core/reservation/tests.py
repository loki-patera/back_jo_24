import re

from django.test import TestCase

from .models import Booking, Booking_Line, Booking_Line_Person
from event.tests.test_models import EventTestCase
from event.utils import time_zone
from promotion.tests import OfferTestCase
from user.tests import PersonTestCase

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class BookingTestCase(TestCase):

  def setUp(self) -> None:

    """ Initialise des données fictives """

    PersonTestCase.setUp(self)
    
    self.element_booking = Booking()
    self.element_booking.person = self.element_person
    self.element_booking.save()
  
  # ------------------------------------------------------ #
  
  def test_str_booking(self) -> None:

    """ Teste si la méthode __str__ de la classe Booking présente la même structure de chaîne """

    wanted_string = re.compile(r"Doe John \(\d{2}/\d{2}/\d{4} - \d{2}:\d{2}:\d{2}\)")

    self.assertRegex(
      Booking.__str__(self.element_booking), wanted_string
    )

# -------------------------------------------------------------------------------------------------------------------- #

class Booking_LineTestCase(TestCase):

  def setUp(self) -> None:

    """ Initialise des données fictives """

    BookingTestCase.setUp(self)

    EventTestCase.setUp(self)

    OfferTestCase.setUp(self)

    self.element_booking_line = Booking_Line()
    self.element_booking_line.buy_token = "zsr6RTaYhLHZt3YJRZm651HAkCjkYWUqvE18a66uk146MojduVUojWuRFYsU89zx"
    self.element_booking_line.offer = self.element_offer
    self.element_booking_line.event = self.element_event
    self.element_booking_line.booking = self.element_booking
    self.element_booking_line.qrcode = "qrcode/qrcode_example.png"
    self.element_booking_line.save()
  
  # ------------------------------------------------------ #
  
  def test_str_booking_line(self) -> None:

    """ Teste si la méthode __str__ de la classe Booking_Line présente la même structure de chaîne """

    wanted_string = re.compile(
      r"Doe John \(\d{2}/\d{2}/\d{4} - \d{2}:\d{2}:\d{2}\) - Cyclisme sur piste | 05/08/2024 (17:00 - 23:30)")

    self.assertRegex(
      Booking_Line.__str__(self.element_booking_line), wanted_string
    )

# -------------------------------------------------------------------------------------------------------------------- #

class Booking_Line_PersonTestCase(TestCase):

  def setUp(self) -> None:

    """ Initialise des données fictives """

    Booking_LineTestCase.setUp(self)

    self.element_booking_line_person = Booking_Line_Person()
    self.element_booking_line_person.booking_line = self.element_booking_line
    self.element_booking_line_person.person = self.element_person
    self.element_booking_line_person.save()
  
  # ------------------------------------------------------ #
  
  def test_str_booking_line_person(self) -> None:

    """ Teste si la méthode __str__ de la classe Booking_Line_Person présente la même structure de chaîne """

    wanted_string = re.compile(
      r"Doe John \(\d{2}/\d{2}/\d{4} - \d{2}:\d{2}:\d{2}\) - Cyclisme sur piste | 05/08/2024 (17:00 - 23:30)")

    self.assertRegex(
      Booking_Line_Person.__str__(self.element_booking_line_person), wanted_string
    )