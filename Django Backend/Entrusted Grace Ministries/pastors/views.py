from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Missionary

def missionary_list(request):
  # Get all missionaries from the database
  missionaries = Missionary.objects.all()

  #  Pass the list of missionaries to the template context
  context = {'missionaries': missionaries}
  return render(request, 'pastors/missionary_list.html', context)



