from predictions.models import Prediction, Vote
from django.contrib import admin

class PredictionAdmin(admin.ModelAdmin):
    list_display = ('prediction_text', 'user', 'date_predicted', 'true_date')

class VoteAdmin(admin.ModelAdmin):
    list_display = ('prediction', 'user')

admin.site.register(Prediction, PredictionAdmin)
admin.site.register(Vote, VoteAdmin)