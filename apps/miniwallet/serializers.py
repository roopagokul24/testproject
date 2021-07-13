from .models import Wallet, Deposit
from rest_framework import serializers

class WalletSerializer(serializers.ModelSerializer):
    enabled_time = serializers.CharField()

    class Meta:
        model = Wallet
        fields = ["id", "user", "enable", "enabled_time", "amount"]


class DepositSerializer(serializers.ModelSerializer):
    reference_id = serializers.CharField()

    class Meta:
        model = Deposit
        fields = ["amount", "reference_id"]
