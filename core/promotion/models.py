from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class Offer(models.Model):

  """ Table Offer contient toutes les offres """

  id_offer = models.SmallAutoField(primary_key=True, null=False)
  type = models.CharField(max_length=10, null=False, verbose_name="Type d'offre")
  number_seats = models.PositiveSmallIntegerField(null=False, validators=[MinValueValidator(1)],
                                                  verbose_name='Nombre de place')
  discount = models.PositiveSmallIntegerField(default=0, verbose_name='Réduction (%)')

  class Meta:
    
    verbose_name = 'Offre'
    verbose_name_plural = 'Offres'