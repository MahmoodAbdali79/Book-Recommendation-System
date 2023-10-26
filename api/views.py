from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from base.models import  SearchHistory
from .serializers import SearchSerializers
from base.forms import SearchForm
from base.Recomendation import recommend
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import render
from django.template.response import TemplateResponse 
from django.http import JsonResponse
import pdb


@api_view(['GET'])
def getData(request):
    items = SearchHistory.objects.all()
    serializer = SearchSerializers(items, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def RecomendPage(request): 

    try:
        Book_name = request.query_params['book']
    except:
        response = {'status': 400,"result":[]}
        return Response(response)
    
    result  = recommend(Book_name)

    response = {'status': 200,"result":[]}

    if result is None:
        result = ""
    data = {'Book' : Book_name, 'response' : result}
    serializer = SearchSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        data['response'] = data['response'].split('-')  
        response = {'status': 200,"result":data}

    return Response(response)









