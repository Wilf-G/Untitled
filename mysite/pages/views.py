from django.shortcuts import render
from .models import Event

def home(request):
    data = {
        'title': 'Hub',
        'message': 'Welcome to your NGC Hub',
        'logged_in': True,
        'itinerary': ['Tech talk with Todd Howard','Paint Pictures of Todd Howard','Todd Howard themed roleplay']
    }
    return render(request, 'pages/home.html', data)


def event_list(request):
    events = Event.objects.all()
    return render(request, 'pages/events.html', {'events': events})


def contact(request):
    contactus = {
        'title': 'Contact Us',
        'message': 'This is where you can contact me if you would particularly like to:',
        'email': 'Email: wilf@hello.ac.uk',
        'number': 'Phone: 07220 123 551'
    }
    return render(request, 'pages/contact.html', contactus)

def aboutus(request):
    content = {
        'title': 'About us',
        'message1': 'There is no us, this is a webpage made by me usinng django, as well as bootstrap, I will now write a paraggraph in order to make this page look more full',
        'message2': 'This is where I will write loads of filler content to make it look like there is an actual about us page here rather than just a small sentence or phrase saying that this is where the about is information is gonna go I dont really know what else to write but its okay and im not really that bothered what goes in here ill probably never ever edit this ever i dont know what else to say so here is more wordslop elephant antidisestablishmentairianism purple meerkat',
        'facts': ['We were founded in 2026','We have loads of money','We own Microsoft', 'We are the best thing in the world']
    }
    return render(request, 'pages/aboutus.html', content)