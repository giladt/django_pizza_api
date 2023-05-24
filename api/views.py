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

    def partial_update(self, request, pk=None):
        data = parsers.JSONParser().parse(request)
        instance = self.queryset.get(id=pk)
        serializer = ClientSerializer(
            instance, data=data, partial=True, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

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


class OrderStatusViewSet(viewsets.ViewSet):
    name = "order_status"
    queryset = OrderStatus.objects.all()

    def list(self, request):
        try:
            allStatus = OrderStatus.objects.all()
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderStatusSerializer(allStatus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            orderStatus = OrderStatus.objects.get(id=pk)
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderStatusSerializer(orderStatus)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ItemViewSet(viewsets.ViewSet):
    name = "item"
    queryset = Item.objects.all()

    def list(self, request):
        try:
            serializer = ItemSerializer(
                self.queryset, many=True, context={"request": request}
            )
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            instance = self.queryset.get(id=pk)
            serializer = ItemSerializer(
                instance, many=False, context={"request": request}
            )
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = parsers.JSONParser().parse(request)

        serializer = ItemSerializer(data=data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        data = parsers.JSONParser().parse(request)
        instance = self.queryset.get(id=pk)
        serializer = ItemSerializer(
            instance, data=data, partial=True, context={"request": request}
        )

        if serializer.is_valid() and OrderItems.objects.get(item=instance.id):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = self.queryset.get(id=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.ViewSet):
    name = "order"
    queryset = Order.objects.all()

    def list(self, request):
        try:
            serializer = OrderSerializer(
                self.queryset, many=True, context={"request": request}
            )
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            instance = self.queryset.get(id=pk)
            serializer = OrderSerializer(
                instance, many=False, context={"request": request}
            )
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = parsers.JSONParser().parse(request)

        serializer = OrderSerializer(data=data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        data = parsers.JSONParser().parse(request)
        instance = self.queryset.get(id=pk)
        serializer = OrderSerializer(
            instance, data=data, partial=True, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = self.queryset.get(id=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class OrderItemsViewSet(viewsets.ViewSet):
    name = "order"
    queryset = OrderItems.objects.all()

    def list(self, request):
        try:
            params = request.GET
            query_status = None
            query_client = None
            query_order = None

            if params.get("order_status"):
                query_order_status = params.get("order_status")[0]
            if params.get("client"):
                query_client = params.get("client")[0]
            if params.get("order"):
                query_order = params.get("order")[0]

            query = self.queryset
            if query_status:
                query = query.filter(order__order_status__id=query_order_status)
            if query_client:
                query = query.filter(order__client__id=query_client)
            if query_order:
                query = query.filter(order__id=query_order)
            serializer = OrderItemsSerializer(query, many=True, context={"request": request})
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request, pk=None):
        try:
            instance = self.queryset.filter(item=pk)
            serializer = OrderItemsSerializer(
                instance, many=True, context={"request": request}
            )
        except Exception as e:
            return Response({"Error": repr(e)}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def create(self, request):
        data = parsers.JSONParser().parse(request)

        serializer = OrderItemsSerializer(data=data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        data = parsers.JSONParser().parse(request)
        instance = self.queryset.get(id=pk)
        serializer = OrderItemsSerializer(
            instance, data=data, partial=True, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = self.queryset.get(id=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


