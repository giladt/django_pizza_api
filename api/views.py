from rest_framework import status, viewsets, parsers
from rest_framework.response import Response

from .models import *
from .serializers import *


class ClientViewSet(viewsets.ViewSet):
    name = "client"
    queryset = Client.objects

    def list(self, request):
        serializer = ClientSerializer(self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            instance = self.queryset.get(id=pk)
        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = parsers.JSONParser().parse(request)

        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        if not pk:
            return Response("Bad request.", status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = self.queryset.get(id=pk)
        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)

        try:
            instance.delete()
        except Exception as e:
            return Response(e.args, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_204_NO_CONTENT)


class FlavourViewSet(viewsets.ViewSet):
    name = "flavour"
    queryset = Flavour.objects.all()

    def list(self, request):
        try:
            allFlavour = Flavour.objects.all()
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = FlavourSerializer(allFlavour, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            flavour = Flavour.objects.get(id=pk)
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = FlavourSerializer(flavour)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SizeViewSet(viewsets.ViewSet):
    name = "size"
    queryset = Size.objects.all()

    def list(self, request):
        try:
            allSize = Size.objects.all()
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = SizeSerializer(allSize, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            size = Size.objects.get(id=pk)
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = SizeSerializer(size)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StatusViewSet(viewsets.ViewSet):
    name = "status"
    queryset = Status.objects.all()

    def list(self, request):
        try:
            allStatus = Status.objects.all()
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = StatusSerializer(allStatus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            orderStatus = Status.objects.get(id=pk)
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = StatusSerializer(orderStatus)
        return Response(serializer.data, status=status.HTTP_200_OK)

