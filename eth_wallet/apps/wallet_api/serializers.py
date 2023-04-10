from .models import Wallet
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers


class WalletGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = "id", 'currency', "public_key", "balance"


@extend_schema_serializer(
    examples=[
         OpenApiExample(
            'Correct post-request to create a wallet ETH uppercase',
            description='Create wallet via: `eth_account.Account` from node [tenderly.com](https://tenderly.co/)',
            value={
                'currency': "ETH",
            },
         ),
         OpenApiExample(
            'Correct post-request to create a wallet eth lowercase',
            description='Create wallet via: `eth_account.Account` from node [tenderly.com](https://tenderly.co/)',
            value={
                'currency': "eth",
            },
         ),
         OpenApiExample(
            'Incorrect (any other) post-request to create a wallet',
            description='We support only ethers cryptocurrency',
            value={
                'currency': "BTC",
            },
         )
    ]
)
class WalletPostSerializer(serializers.ModelSerializer):
    currency = serializers.CharField()

    class Meta:
        model = Wallet
        fields = "id", 'currency'

    def update(self, instance, validated_data):
        """
        Update currency value if user passed it in lowercase
        :param instance:
        :param validated_data:
        :return:
        """
        instance.currency = validated_data.get('currency', instance.currency)
        return instance
