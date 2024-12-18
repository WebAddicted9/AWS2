from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models

class myuser(AbstractUser):
    mobile_no = models.CharField(max_length=10)
    qr_code = models.ImageField(upload_to='qrcodes/', null=True, blank=True)


# class FormData(models.Model):
#     name = models.CharField(max_length=100)
#     mobile_no = models.CharField(max_length=15)
#     qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)






