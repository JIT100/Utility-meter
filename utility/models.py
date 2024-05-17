from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.
class Meter(models.Model):
    label = models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return f"{self.label} Meter"

    def save(self, *args, **kwargs):
        if self.label:
            self.label = self.label.capitalize()
        super().save(*args, **kwargs)

    def get_meter_data_list(self):
        return self.meters.order_by('-created')


class Meter_Data(TimeStampedModel):
    meter = models.ForeignKey(Meter,on_delete=models.CASCADE, related_name="meters", blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.meter.label} Meter - Value is {self.value} Updated at {self.created}"
