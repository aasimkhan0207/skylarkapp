from django.shortcuts import render, HttpResponse, redirect, reverse
from django.http import JsonResponse
import json
from .models import *

def home(request):
    games = Game.objects.all()
    d = dict()
    teams = set()       # A set of unique team name
    for g in games:
        teams.add(g.team1)
        teams.add(g.team2)
        date = g.date.strftime('%d %B %Y')  # Converting date into string
        if g.team1 in d:
            d[g.team1].append({g.team2: date})
        else:
            d[g.team1] = [{g.team2: date}]

        if g.team2 in d:
            d[g.team2].append({g.team1: date})
        else:
            d[g.team2] = [{g.team1: date}]

    matches2 = {}
    for team in d:
        matches2[team] = []
        for x in d[team]:
            for y in x:
                matches2[team].append(y)
    
    context = {"matches": d, "teams": teams}

    return render(request, 'fifa/index.html', context)


def add_match(request):
    if request.method == 'GET':
        teams_obj = Team.objects.all()
        all_countries = []
        for x in teams_obj:
            all_countries.append(x.name)
        context = {"all_teams": all_countries}
        return render(request, 'fifa/add.html', context)
    else:
        t1 = request.POST["team1"]
        t2 = request.POST["team2"]
        date = request.POST["date"]     #dd/mm/YYY
        date = format_date(date)        #YYYY-mm-dd
        game = Game.objects.create(team1 = t1, team2 = t2, date = date)
        game.save()
        return redirect(reverse('fifa:home'))


def getjson(request):
    d = dict()
    matches = Match.objects.all()
    for x in matches:
        rivals = []
        for y in x.followers.all():
            rivals.append(y.name)
        d[x.name] = rivals
    return JsonResponse(d)
    
def format_date(d):
    d = d.split('/')
    x = d[2] + '-' + d[0] + '-' + d[1]
    return x