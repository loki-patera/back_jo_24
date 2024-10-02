import uuid

from django.db import models

from private_storage.fields import PrivateFileField

from event.models import Event
from promotion.models import Offer
from user.models import Person
from event.utils import time_zone

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class Booking(models.Model):

  """ Table Booking contient toutes les réservations """

  id_booking = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  booking_date = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Date de réservation')
  person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, verbose_name='Nom du client')

  class Meta:
    
    verbose_name = 'Réservation'
    verbose_name_plural = 'Réservations'
  
  def __str__(self) -> str:

    date_booking = time_zone(self.booking_date).strftime("%d/%m/%Y - %H:%M:%S")

    return f'{self.person} ({date_booking})'

# -------------------------------------------------------------------------------------------------------------------- #

class Booking_Line(models.Model):

  """ Table Booking_Line contient toutes les lignes de réservations """

  id_booking_line = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  buy_token = models.CharField(unique=True, max_length=250, null=False, verbose_name="Clé d'achat")
  offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=False, verbose_name="Type d'offre")
  event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False, verbose_name="Évènement")
  booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=False, verbose_name='Réservation')
  qrcode = PrivateFileField(upload_to='qrcode', null=True, verbose_name='QR Code')

  class Meta:

    verbose_name = 'Ligne de réservation'
    verbose_name_plural = 'Lignes de réservation'
  
  def __str__(self) -> str:

    return f'{self.booking} - {self.event}'

# -------------------------------------------------------------------------------------------------------------------- #

class Booking_Line_Person(models.Model):

  """ Table Booking_Line_Person contient les spectateurs liés à une ligne de réservation """

  id_booking_line_person = models.SmallAutoField(primary_key=True, null=False)
  booking_line = models.ForeignKey(Booking_Line, on_delete=models.CASCADE, null=False,
                                   verbose_name='Ligne de réservation')
  person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, verbose_name='Nom du spectateur')

  class Meta:

    constraints = [
      models.UniqueConstraint(fields=['booking_line', 'person'], name='unique_booking_line_person')
    ]
    verbose_name = 'Spectateur lié à la ligne de réservation'
    verbose_name_plural = 'Spectateurs liés aux lignes de réservation'
  
  def __str__(self) -> str:

    return f'{self.booking_line}'