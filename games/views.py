from django.shortcuts import render
from .models import Game, Review

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def review(request, pk):
    return render(request, 'games/game_list.html')#mockup template