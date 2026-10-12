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
        'message1': "Welcome to NCG Events, where gaming culture comes to life! We are a gaming event organisation company dedicated to bringing gamers, creators, developers, and gaming enthusiasts together through unforgettable experiences, exciting competitions, and community-driven events. Whether you're a casual player looking to meet like-minded people, a competitive gamer ready to prove your skills, or simply someone who loves the atmosphere of gaming conventions, NCG Events aims to create an environment where everyone can find their place. Gaming has grown far beyond the screen. It has become a worldwide community built around creativity, competition, friendship, and a shared passion for interactive entertainment. At NCG Events, we believe that some of the best gaming experiences happen when people come together in person, sharing their favourite games, discovering new interests, and creating memories that last long after the final match has ended. Our goal is to bring that experience to life by organising events that celebrate everything gaming has to offer.",
        'message2': "At NCG Events, we specialise in organising and coordinating gaming events designed to entertain, inspire, and connect people. From lively gaming conventions and multiplayer tournaments to community meetups and interactive gaming experiences, we aim to deliver events that capture the excitement and energy of the gaming world. Our events can bring together players across a wide range of genres, including competitive esports, first-person shooters, fighting games, racing games, strategy games, role-playing adventures, and much more. Whether you're interested in testing your abilities against other players, exploring the latest gaming technology, meeting fellow fans, or simply enjoying a day surrounded by gaming culture, NCG Events strives to provide something for everyone. We understand that a successful event involves much more than simply putting consoles and computers in a room. It requires careful planning, organisation, attention to detail, and an understanding of what makes gaming communities special. From coordinating activities and managing event schedules to creating engaging experiences for attendees, we work towards making every event enjoyable, accessible, and memorable.",
        'facts': ['We were founded in 2026 by Jay Marriner and Famous content Creator PewDiePie','Collaborating with 15 large scale gaming and development companies to provide our visitors with real, accurate information','Completed over 60 events accross the United Kingdom and Ireland', 'We are completely unstoppable and will grow to take over the world and destroy everyone']
    }
    return render(request, 'pages/aboutus.html', content)