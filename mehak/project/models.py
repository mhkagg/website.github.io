from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100, blank=True)
    lname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

def get_full_name(self):
    return self.profile.fname

class Blogs(models.Model):
    name = models.CharField(max_length=100, blank=True)
    message = models.CharField(max_length=1000,blank=True)

class Search(models.Model):
    address= models.CharField(max_length=200, null=True)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class Attraction(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.name)