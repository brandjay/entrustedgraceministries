"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render # type: ignore
from django.http import HttpRequest # type: ignore
from django.core.files.storage import FileSystemStorage # type: ignore
from .models import Main 
from .models import Events
def home(request):
    # Get the Main object
    main = Main.objects.first()
    events = Events.objects.all()

    if request.method == 'POST':
        # Update the Main object with the form data
        main.intro = request.POST['intro']
        main.par1 = request.POST['par1']
        main.save()
        events.title = request.Post['title']
        events.event = request.Post['event']
        events.save()


        # Update the index.html file
        fs = FileSystemStorage()
        with fs.open('index.html', 'w') as index_file:
            index_file.write(f'<h1>{main.intro}</h1>\n<p>{main.par1}</p>')
           # index_file.write(f'<h1>{events.title}</h1>\n<p>{events.event}</p>')

    return render(request, 'app/index.html', {'main': main, 'events': events})
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
