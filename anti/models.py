from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class report(models.Model):
    name = models.CharField(max_length = 60)
    location = models.CharField(max_length = 60)
    category = models.ManyToManyField(category)
    position_of_offender = models.CharField(max_length = 60,null=True)
    email = models.EmailField()
    time_uploaded = models.DateTimeField(auto_now_add=True,null=True)
    reporter = models.ForeignKey(User,on_delete=models.CASCADE)
    report_incident = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        ordering=['-time_uploaded']

    def save_report(self):
        self.save()

    def delete_report(self):
        self.delete()

    @classmethod
    def get_report(cls):
        report = Report.objects.all()
        return report
