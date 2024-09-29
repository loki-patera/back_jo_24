from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class Offer(models.Model):

  """ Table Offer contient toutes les offres """

  id_offer = models.SmallAutoField(primary_key=True, null=False)
  type = models.CharField(max_length=10, null=False)
  number_seats = models.PositiveSmallIntegerField(null=False, validators=[MinValueValidator(1)])
  discount = models.PositiveSmallIntegerField(default=0)