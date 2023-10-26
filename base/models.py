from django.db import models

# Create your models here.





class SearchHistory(models.Model):
    Book = models.CharField(max_length=200, null=False, blank=False)
    Create_at = models.DateField(auto_now_add=True)
    response = models.CharField(max_length=400)