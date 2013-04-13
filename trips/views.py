# Create your views here.
from django.template.loader import get_template
from django.core.mail.message import EmailMultiAlternatives
from django.shortcuts import render_to_response
from django.template import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from datetime import datetime, timedelta
from trips.models import *
import simplejson
def home(request):
  values={"user":request.user}
  if request.user.id is not None:
    values["user_profile"]=request.user.get_profile()
  return render_to_response('trips/home.html', values, context_instance=RequestContext(request))

