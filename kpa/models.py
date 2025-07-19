from django.db import models
from django.db.models import JSONField


# Create your models here.

class WheelSpecification(models.Model):
    formNumber=models.CharField(max_length=50)
    submittedBy=models.CharField(max_length=50)
    submittedDate=models.DateField()
    fields          = JSONField(blank=True, null=True)

    def __str__(self):
        return self.formNumber

# class BogieChecksheet(models.model):
#     WheelSpecification=models.ForeignKey(WheelSpecification,on_delete=models.CASCADE,related_name="wheel")
#     inspectionBy=models.CharField(max_length=50)

