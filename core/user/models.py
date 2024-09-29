import uuid

from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class Person(models.Model):

  """ Table Person contient tous les spectateurs """

  id_person = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  firstname = models.CharField(max_length=50, null=False)
  lastname = models.CharField(max_length=50, null=False)
  date_of_birth = models.DateField(null=False)
  country = models.CharField(max_length=75, null=False)

# -------------------------------------------------------------------------------------------------------------------- #

class Customer(Person):

  """ Table Customer contient tous les clients """

  email = models.EmailField(unique=True, max_length=100, null=False)
  password = models.CharField(max_length=50, null=False)
  phone = PhoneNumberField()
  account_token = models.CharField(unique=True, max_length=250, null=False)