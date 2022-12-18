from django.db import models
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=200) 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])  # musi zostać dodane get_absolute_url przy używaniu formularza, poniewaz po wysłaniu post/get musi nastąpić przekierowanie
                                                            # w tym wypadku reverse bierze bezwzględną ścieżkę do URL, jest to mapowanie na URL i odwołanie do odpowiedniego widoku