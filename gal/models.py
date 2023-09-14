# from django.db import models

# # Create your models here.
# class Image(models.Model):
#     photo=models.ImageField(upload_to="myimage")
#     date=models.DateTimeField(auto_now_add=True)
import uuid
from django.db import models
from django.contrib.auth.models import User


def user_upload_to(instance, filename):
    # Generate a unique filename using a UUID
    ext = filename.split('.')[-1]
    unique_filename = f'{uuid.uuid4()}.{ext}'
    return f'user_images/{instance.user.username}/{unique_filename}'

class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)







