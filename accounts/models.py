from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    serial_no  = models.CharField(max_length=255,null=False,unique=False)
    location   = models.CharField(max_length=255,null=False)
    attribute = models.CharField(max_length=255,null=False)
    status = models.CharField(max_length=255,null=False)
    battery_status = models.CharField(max_length=255,null=False)
    battery_voltage = models.CharField(max_length=255,null=False)
    power_panel = models.CharField(max_length=255,null=False)
    panel_voltage = models.CharField(max_length=255,null=False)
    energy_curr = models.CharField(max_length=255,null=False)
    total_energy = models.CharField(max_length=255,null=False)
    belongs_to = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.serial_no}"
