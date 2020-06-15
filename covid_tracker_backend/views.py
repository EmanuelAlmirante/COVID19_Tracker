from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from covid_tracker_backend.models import COVIDData
from covid_tracker_backend.serializers import COVIDSerializer
from rest_framework.decorators import api_view

from covid_tracker_backend import scraper


@api_view(['GET', 'POST'])
def data_list(request):
    scraper.webscraper('Portugal')

    # GET list of countries, POST data about a new country
    if request.method == 'GET':
        countries = COVIDData.objects.all()

        covid_tracker_serializer = COVIDSerializer(countries, many = True)
        return JsonResponse(covid_tracker_serializer.data, safe = False)

    elif request.method == 'POST':
        country_json = JSONParser().parse(request)
        country_serializer = COVIDSerializer(data = country_json)

        if country_serializer.is_valid():
            country_serializer.save()
            return JsonResponse(country_serializer.data, status = status.HTTP_201_CREATED)

        return JsonResponse(country_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def country_details(request, pk):
    # Find country by id
    try:
        country = COVIDData.objects.get(pk = pk)
    except COVIDData.DoesNotExist:
        return JsonResponse({'message': 'The country with this id does not exist'}, status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        country_serializer = COVIDSerializer(country)
        return JsonResponse(country_serializer.data)

    elif request.method == 'PUT':
        country_json = JSONParser().parse(request)
        country_serializer = COVIDSerializer(country, data = country_json)

        if country_serializer.is_valid():
            country_serializer.save()
            return JsonResponse(country_serializer.data)

        return JsonResponse(country_serializer.errors, status = status)

    elif request.method == 'DELETE':
        country.delete()
        return JsonResponse({'message': 'Country was deleted successfully!'}, status = status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def country_data(request, country):
