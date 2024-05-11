from django.urls import path
from . import views  # Assuming your views are in the same app directory

urlpatterns = [
  path('pastors/', views.missionary_list, name='pastor_list'),  # List all pastors
  # You can add more URL patterns here for specific functionalities
  # For example, a detail view for a pastor:
  # path('pastors/<int:pastor_id>/', views.pastor_detail, name='pastor_detail'),
]
