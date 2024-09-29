import uuid

from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class Person(models.Model):

  """ Table Person contient tous les spectateurs """

  id_person = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  firstname = models.CharField(max_length=50, null=False, verbose_name='Prénom')
  lastname = models.CharField(max_length=50, null=False, verbose_name='Nom de famille')
  date_of_birth = models.DateField(null=False, verbose_name='Date de naissance')
  country = models.CharField(max_length=75, null=False, verbose_name='Pays')

  class Meta:

    verbose_name = 'Spectateur'
    verbose_name_plural = 'Spectateurs'
  
  def __str__(self) -> str:
    
    return f'{self.lastname} {self.firstname}'

# -------------------------------------------------------------------------------------------------------------------- #

class Customer(Person):

  """ Table Customer contient tous les clients """

  email = models.EmailField(unique=True, max_length=100, null=False, verbose_name='E-mail')
  password = models.CharField(max_length=50, null=False, verbose_name='Mot de passe')
  phone = PhoneNumberField(verbose_name='Numéro de téléphone')
  account_token = models.CharField(unique=True, max_length=250, null=False, verbose_name='Clé de compte')

  class Meta:
    
    verbose_name = 'Client'
    verbose_name_plural = 'Clients'