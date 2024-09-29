from django.core.validators import MinValueValidator
from django.db import models

from .utils import time_zone

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class Sport(models.Model):

  """ Table Sport contient tous les sports """

  id_sport = models.SmallAutoField(primary_key=True, null=False)
  title = models.CharField(max_length=30, null=False, verbose_name='Sport')
  image = models.ImageField(upload_to='images/sports', verbose_name='Image')

  class Meta:

    verbose_name = 'Épreuve sportive'
    verbose_name_plural = 'Épreuves sportives'
  
  def __str__(self) -> str:

    return self.title

# -------------------------------------------------------------------------------------------------------------------- #

class Event(models.Model):

  """ Table Event contient tous les évènements """

  id_event = models.SmallAutoField(primary_key=True, null=False)
  sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=False, verbose_name='Épreuves sportives')
  location = models.CharField(max_length=50, null=False, verbose_name='Lieu')
  start_date = models.DateTimeField(null=False, verbose_name='Date de début')
  end_date = models.DateTimeField(null=False, verbose_name='Date de fin')
  price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00)], null=False,
                              verbose_name='Prix (€)')
  
  class Meta:

    verbose_name = 'Évènement'
    verbose_name_plural = 'Évènements'
  
  def __str__(self) -> str:

    start_event = time_zone(self.start_date).strftime("%d/%m/%Y (%H:%M")
    end_event = time_zone(self.end_date).strftime("%H:%M)")
    
    return f'{self.sport} | {start_event} - {end_event}'

# -------------------------------------------------------------------------------------------------------------------- #

class Competition(models.Model):

  """ Table Competition contient toutes les compétitions """

  class Gender(models.TextChoices):

    Femme = "Femme"
    Homme = "Homme"
    Mixte = "Mixte"
  
  id_competition = models.SmallAutoField(primary_key=True, null=False)
  description = models.CharField(max_length=50, null=False, verbose_name='Description')
  gender = models.CharField(choices=Gender.choices, max_length=5, verbose_name='Genre')
  phase = models.CharField(max_length=50, null=False, verbose_name='Phase')
  event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False, verbose_name='Évènement')

  class Meta:
    
    verbose_name = 'Compétition'
    verbose_name_plural = 'Compétitions'
  
  def __str__(self) -> str:

    return f'{self.event} | {self.gender}, {self.description}, {self.phase}'