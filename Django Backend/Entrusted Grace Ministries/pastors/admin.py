from django.contrib import admin
from .models import Missionary

@admin.register(Missionary)
class MissionaryAdmin(admin.ModelAdmin):
  # Customize the admin interface for the Missionary model here (optional)
  list_display = ['first_name', 'last_name', 'date']  # Fields to display in the list view
  # Other customization options (explained below)

