from datetime import datetime

from django.contrib import admin

from user.models import Customer, Person

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

admin.site.site_header = "Administration de la billetterie des Jeux olympiques Paris 2024"

# -------------------------------------------------------------------------------------------------------------------- #

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

  list_display = ['lastname', 'firstname', 'date_of_birth', 'status', 'country']
  list_filter = ['country']
  ordering = ['lastname', 'firstname']

  def status(self, instance) -> str:
    
    age = datetime.now().year - instance.date_of_birth.year

    if(age > 12):

      return 'Adulte'
    
    else:

      return 'Enfant'
  
  status.short_description = "Statut"

# -------------------------------------------------------------------------------------------------------------------- #

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

  list_display = ['lastname', 'firstname', 'email', 'account_token']
  ordering = ['lastname', 'firstname']