from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    serial_no  = models.CharField(max_length=255,null=False,unique=False)
    location   = models.CharField(max_length=255,null=False)
    attribute = models.CharField(max_length=255,null=False)
    belongs_to = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.created_at}  {self.updated_at}   {self.attribute1}   {self.attribute2}   {self.attribute3}   {self.attribute4}"
