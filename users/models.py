from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from trails.models import Trail as Route
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    birth_date = models.DateTimeField(default=timezone.now)
    experience=models.CharField(max_length=20)
    contact_number = models.CharField( max_length=25, 
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$', 
                message="Contact number format: '+353899625243'. Up to 15 digits allowed."
            )
        ],default='899625243')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'



