from platform import processor
from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

# Create your models here.
class User(AbstractUser):
    profile_image = ProcessedImageField(
        blank = True,
        upload_to='profile_imgs/',
        processors=[Thumbnail(200,200)],
        format='JPEG',
        options={'quality': 90}
    )
    nickname = models.CharField(max_length=16)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    