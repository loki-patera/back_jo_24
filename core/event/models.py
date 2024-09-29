from django.core.validators import MinValueValidator
from django.db import models

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class Sport(models.Model):

  """ Table Sport contient tous les sports """

  id_sport = models.SmallAutoField(primary_key=True, null=False)
  title = models.CharField(max_length=30, null=False)
  image = models.ImageField(upload_to='images/sports')

# -------------------------------------------------------------------------------------------------------------------- #

class Event(models.Model):

  """ Table Event contient tous les évènements """

  id_event = models.SmallAutoField(primary_key=True, null=False)
  sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=False)
  location = models.CharField(max_length=50, null=False)
  start_date = models.DateTimeField(null=False)
  end_date = models.DateTimeField(null=False)
  price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00)], null=False)

# -------------------------------------------------------------------------------------------------------------------- #

class Competition(models.Model):

  """ Table Competition contient toutes les compétitions """

  class Gender(models.TextChoices):

    Femme = "Femme"
    Homme = "Homme"
    Mixte = "Mixte"
  
  id_competition = models.SmallAutoField(primary_key=True, null=False)
  description = models.CharField(max_length=50, null=False)
  gender = models.CharField(choices=Gender.choices, max_length=5)
  phase = models.CharField(max_length=50, null=False)
  event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)