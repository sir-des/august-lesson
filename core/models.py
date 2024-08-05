from django.db import models

# Create your models here.
class Profile(models.model):
    user = pass
    id_user = pass
    bio = pass
    profileimg = models.Imagefield(upload_to='profile_images')
    location = pass
