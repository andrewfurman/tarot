from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Prediction(models.Model):
    prediction_text = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    date_predicted = models.DateTimeField('date you predicted it')
    true_date = models.DateTimeField('date it comes true')
    def __unicode__(self):
        return self.prediction_text

class Vote(models.Model):
    prediction = models.ForeignKey(Prediction)
    user = models.ForeignKey(User)
