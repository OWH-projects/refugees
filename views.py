from models import *
from django.shortcuts import *
from django.db.models import *
from myproject.refugees.models import *
from django.http import HttpResponse
from django.db.models import F

def Main(request):
    dictionaries = {}
    return render_to_response('refugees/main.html', dictionaries)