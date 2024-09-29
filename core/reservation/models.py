import uuid

from django.db import models

from private_storage.fields import PrivateFileField

from event.models import Event
from promotion.models import Offer
from user.models import Person

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class Booking(models.Model):

  """ Table Booking contient toutes les réservations """

  id_booking = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  booking_date = models.DateTimeField(auto_now_add=True, null=False)
  person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)

# -------------------------------------------------------------------------------------------------------------------- #

class Booking_Line(models.Model):

  """ Table Booking_Line contient toutes les lignes de réservations """

  id_booking_line = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  buy_token = models.CharField(unique=True, max_length=250, null=False)
  offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=False)
  event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
  booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=False)
  qrcode = PrivateFileField(upload_to='qrcode', null=True)

# -------------------------------------------------------------------------------------------------------------------- #

class Booking_Line_Person(models.Model):

  """ Table Booking_Line_Person contient les spectateurs liés à une ligne de réservation """

  id_booking_line_person = models.SmallAutoField(primary_key=True, null=False)
  booking_line = models.ForeignKey(Booking_Line, on_delete=models.CASCADE, null=False)
  person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)

  class Meta:

    constraints = [
      models.UniqueConstraint(fields=['booking_line', 'person'], name='unique_booking_line_person')
    ]