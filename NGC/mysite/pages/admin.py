from django.contrib import admin
from .models import Event, Comment, Organisers, Catagory

admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Organisers)
admin.site.register(Catagory)