from django.db import models


class Organisers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Catagory(models.Model):
    catagory = models.CharField(max_length=50)

    def __str__(self):
        return self.catagory

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=100)
    catagory= models.ForeignKey(Catagory, on_delete = models.CASCADE)
    organiser= models.ForeignKey(Organisers, on_delete = models.CASCADE)


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"Comment by {self.author_name}"
    
