from django.db import models
from  django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone 
difficulty_level=[
    ("easy","EASY"),
    ("moderate","MODERATE"),
    ("challenging","CHALLEGNING"),
    ("hard","HARD"),]
type_trail=[
    ("hiking","HIKING"),
    ("bike","Bike"),
    ("running","RUNNING"),
]

    
class Trail(models.Model):
    title=models.CharField(max_length=20,default='New trail')
    difficulty_level=models.CharField(max_length=20,
                               choices=difficulty_level)
    type=models.CharField(max_length=20, choices=type_trail)
    duration=models.CharField(max_length=20)
    distance=models.CharField(max_length=15)
    meeting_point=models.CharField(max_length=50)
    date=models.DateTimeField(default=timezone.now)
    date_posted=models.DateTimeField(default=timezone.now)
    description = models.TextField()
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.description} '
    
    def get_absolute_url(self):
        return reverse('trail-detail', kwargs={'pk': self.pk})
    


    # because I use the view class to create instances of a Trail model, I use @property to access the data in the template
    # for each route I access the list of participants
    @property
    def get_participants(self):
        participants_id=[]
        participants_id = Participant.objects.filter(trail_id=self.id).values_list('user_id',flat=True)
        participants=[]
        for id in participants_id:
             participants.append(Participant.objects.get(user_id=id,trail_id=self.id))
             print(id)
        return participants
    # for each route I access the list of comments
    @property
    def get_comments(self):
        comments=[]
        comments = Comment.objects.filter(trail_id=self.id)
        return comments
             
     # for each route I access the coordinator info
    @property
    def get_coordinator(self):
        coordinator=Trail.objects.get(user_id=self.coordinator_id,trail_id=self.id)
        return coordinator
    # for each route I access the list of trails
    @property
    def get_trails(self):
        trails=Trail.objects.all()
        return trails


class Participant(models.Model):
    trail = models.ForeignKey(Trail,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    joining_date=models.DateTimeField(default=timezone.now)
    # retrieve participant data from the database
    def get_participant_details(self,id_user):
        participant=Participant.objects.get(user_id=id_user)
        return participant

class Comment(models.Model):
    trail = models.ForeignKey(Trail,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    create_on =models.DateTimeField(default=timezone.now)
    comment= models.TextField()
   
    def __str__(self):
        return f'{self.comment} '
    # retrieve participant data from the database
    # for each comment instance, I retrieve user data from the database to be displayed them in the template
    @property
    def get_user(self):
        user=Comment.objects.get(user_id=self.user)
        return user