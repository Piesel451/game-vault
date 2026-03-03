from django.shortcuts import get_object_or_404, render
from django.db.models import Avg
from .models import Game, Review

def games_list(request):
    games = Game.objects.annotate(
        average_rating=Avg('game_reviews__rating')
    ).all()
    return render(request, 'games/games_list.html', {'games': games})

def game_reviews(request, pk):
    reviews = Review.objects.filter(game_id = pk).select_related("author")
    return render(request, 'games/review_list.html', {'reviews': reviews})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk = pk)
    return render(request, 'games/game_detail.html', {'game': game})