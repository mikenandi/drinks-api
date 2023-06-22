from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        # get all drinks
        drinks = Drink.objects.all()

        # Serialize them 
        serializer = DrinkSerializer(drinks, many=True)

        # Return json response
        return JsonResponse({'drinks': serializer.data})

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'status': 400, 'message': 'BadRequest'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_details(request, id: int):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response({'msg': 'data not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)

        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
