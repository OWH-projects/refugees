from models import *
from django.shortcuts import *
from django.db.models import *
from django.http import HttpResponse
import datetime

last_updated = datetime.datetime(2015, 11, 17)
total_count = Refugee.objects.aggregate(quoi=Sum("num"))
list_of_states = Refugee.objects.values('stateabbr', 'stateabbr__statename').distinct().order_by('stateabbr__statename')
sum_by_country = Refugee.objects.values("countrycode", "countrycode__name").annotate(Sum("num")).order_by(("countrycode__name"))

def Main(request):
    sum_by_year = Refugee.objects.values("year").annotate(Sum("num")).order_by('year')
    sum_by_state = Refugee.objects.values("stateabbr", "stateabbr__statename").annotate(Sum("num")).order_by('stateabbr__statename')
    dictionaries = {'total_count':total_count, 'sum_by_year':sum_by_year,'sum_by_state':sum_by_state, 'sum_by_country':sum_by_country,'last_updated':last_updated,}
    return render_to_response('refugees/main.html', dictionaries)

def State(request, st):
    state = st
    refs = Refugee.objects.filter(stateabbr=st)
    state_total = refs.aggregate(Sum("num"))
    first = refs[0]
    state_sum_by_country = refs.values("countrycode__name").annotate(Sum("num"))
    sum_by_city = refs.values("city").annotate(Sum("num")).order_by('city')
    state_sum_by_year = refs.values("year").annotate(Sum("num")).order_by('year')
    dictionaries = {'state_sum_by_country':state_sum_by_country, 'sum_by_country':sum_by_country, 'sum_by_year':state_sum_by_year, 'sum_by_city':sum_by_city, 'state':state, 'first':first, 'state_total':state_total, 'list_of_states':list_of_states,}
    return render_to_response('refugees/state.html', dictionaries)

def Country(request, country):
    refs = Refugee.objects.filter(countrycode=country)
    country_total = refs.aggregate(Sum("num"))
    first = refs[0]
    sum_by_city = refs.values("city").annotate(Sum("num")).order_by('city')
    country_sum_by_year = refs.values("year").annotate(Sum("num")).order_by('year')
    dictionaries = {'country': country, 'country_total': country_total, 'first':first, 'sum_by_city':sum_by_city, 'country_sum_by_year':country_sum_by_year, }
    return render_to_response('refugees/country.html', dictionaries)
