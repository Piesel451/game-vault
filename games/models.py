from django.conf import settings
from django.db import models
from django.utils import timezone

class Game(models.Model):
    title = models.CharField(max_length=200)
    developer = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Review(models.Model):
    game = models.ForeignKey(
        Game, 
        on_delete=models.CASCADE, 
        related_name='game_reviews')
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name = "user_reviews")
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"Recenzja {self.game.title} autorstwa {self.author}"