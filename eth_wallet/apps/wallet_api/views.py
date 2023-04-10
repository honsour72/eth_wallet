from .helpers import create_web3_wallet
from .models import Wallet
from .serializers import WalletGetSerializer, WalletPostSerializer
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin


class WalletView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Wallet.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return WalletPostSerializer
        if self.request.method == "GET":
            return WalletGetSerializer

    @extend_schema(
        description='Получение списĸа ĸошельĸов. Ответ представляет из себя списоĸ, состоящий из словарей',
        responses=WalletGetSerializer
    )
    def get(self, request) -> Response:
        """
        Example curl request:
        curl http://localhost:8000/api/v1/wallets
        For more readable response i usually use: `-H 'Accept: application/json; indent=4'`
        :param request:
        :return:
        """
        return self.list(request)

    @extend_schema(
        description='Создание ĸошельĸа в блоĸчейне Ethereum (в БД хранятся публичный и приватный ĸлючи)',
        parameters=[
            OpenApiParameter("currency", OpenApiTypes.STR, description='Криптовалюта (ETH | eth)'),
        ],
        responses=WalletGetSerializer
    )
    def post(self, request) -> Response:
        """
        Example of curl request:
        $ curl -X POST -H 'Accept: application/json; indent=4' -d 'currency=ETH' http://localhost:8000/api/v1/wallets
        $ curl -X POST -H 'Accept: application/json; indent=4' -d 'currency=eth' http://localhost:8000/api/v1/wallets
        :param request:
        :return: Response
        """
        currency: str = request.data.get('currency', '')

        if currency not in ("eth", "ETH"):
            return Response(
                {"error": f"Our wallet support only ETH currency"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            currency = currency.upper()

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            try:
                private_key, public_key = create_web3_wallet()
            except TypeError as our_err:
                result = {"error": our_err}
                result_status = status.HTTP_503_SERVICE_UNAVAILABLE
            else:
                new_wallet = Wallet(currency=currency, public_key=public_key, private_key=private_key)
                try:
                    new_wallet.save()
                except Exception as create_error:
                    result = {"error": create_error}
                    result_status = status.HTTP_500_INTERNAL_SERVER_ERROR
                else:
                    result = dict(id=new_wallet.id, currency=currency, public_key=public_key)
                    result_status = status.HTTP_200_OK

        else:
            result = {"error": serializer.errors}
            result_status = status.HTTP_400_BAD_REQUEST

        return Response(result, status=result_status)
