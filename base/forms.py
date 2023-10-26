from django.forms import ModelForm
from base.models import SearchHistory

class SearchForm(ModelForm):
    class Meta:
        model = SearchHistory
        fields = ["Book"]



    # Book = models.CharField(max_length=200, label='Book Form')