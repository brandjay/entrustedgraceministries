"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.core.files.storage import FileSystemStorage
from .models import Main 

def home(request):
    # Get the Main object
    main = Main.objects.first()

    if request.method == 'POST':
        # Update the Main object with the form data
        main.intro = request.POST['intro']
        main.par1 = request.POST['par1']
        main.save()

        # Update the index.html file
        fs = FileSystemStorage()
        with fs.open('index.html', 'w') as index_file:
            index_file.write(f'<h1>{main.intro}</h1>\n<p>{main.par1}</p>')

    return render(request, 'app/index.html', {'main': main})
"""
def home(request):
     # Renders the home page.
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
"""
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
