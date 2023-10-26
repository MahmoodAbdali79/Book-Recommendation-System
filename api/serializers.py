from rest_framework import serializers
from base.models import SearchHistory



class SearchSerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        search = SearchHistory.objects.create(**validated_data)
        return search

    class Meta:
        model = SearchHistory
        fields = "__all__"
        # fields = ["Book", 'response']


