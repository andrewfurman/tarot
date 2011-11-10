from django.http import HttpResponse
from predictions.models import Prediction, Vote
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import logout

def index(request):
    latest_prediction_list = Prediction.objects.all().order_by('-date_predicted')
    return render_to_response('predictions/index.html', {'latest_prediction_list': latest_prediction_list})

def detail(request, prediction_id):
    p = get_object_or_404(Prediction, pk=prediction_id)
    return render_to_response('predictions/detail.html', {'prediction': p})

def results(request, prediction_id):
    return HttpResponse("You're looking at the results of poll %s." % prediction_id)

def vote(request, prediction):
    v = prediction.vote_set.create(user=user_id)
    v.save()
    return render_to_response('predictions/vote.html', {'prediction': prediction_id}, context_instance=RequestContext(request))

def userlist(request):
    user_list = User.objects.all()
    return render_to_response('predictions/users.html', {'user_list': user_list})

def userprofile(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    users_predictions = Prediction.objects.filter(user=user_id)
    points = 0
    for vote_object in Vote.objects.all():
        if int(vote_object.prediction.user.id) == int(user_id):
            points += 1
    return render_to_response('predictions/userprofile.html', {'userobject': u, 'points':points})

def logout_view(request):
    logout(request)
    return render_to_response('registration/logout.html')

def newprediction(request):
    p = Prediction(prediction_text=prediction, user=request.user, pub_date=datetime.datetime.now(),true_date=datetime.datetime.now())