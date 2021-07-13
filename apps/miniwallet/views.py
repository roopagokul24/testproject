
from datetime import datetime

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import WalletSerializer, DepositSerializer
from .models import Wallet, Deposit, Withdrawal, Withdrawal

class InitializeWalletAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        response = {}
        user = self.request.user
        try:
            wallet = Wallet.objects.get(user=user)
            response = {
                    'errors': "Wallet Already Initialized!!",
                    'status': status.HTTP_400_BAD_REQUEST
                }
        except Wallet.DoesNotExist:
            wallet = Wallet()
            wallet.user = user
            wallet.ammount = "0"
            wallet.save()
            response = {
                    'message': "Wallet Initialized",
                    'status': status.HTTP_200_OK
                }
        return Response(response)


class EnableWalletAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        response = {}
        user = self.request.user
        try:
            wallet = Wallet.objects.get(user=user)
            if wallet.enable == False:
                wallet.enable = True
                wallet.enabled_time = datetime.now()
                wallet.save()
                response = {
                        'message': "Wallet Enabled",
                        'status': status.HTTP_200_OK
                    }
            else:
                response = {
                            'message': "Wallet Already Enabled",
                            'status': status.HTTP_400_BAD_REQUEST
                            }
        except Wallet.DoesNotExist:
            response = {
                        'errors': "Wallet not initialized!!",
                        'status': status.HTTP_400_BAD_REQUEST
                        }
        return Response(response)


class DisableWalletAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request):
        response = {}
        user = self.request.user
        try:
            wallet = Wallet.objects.get(user=user)
            if wallet.enable == True:
                wallet.enable = False
                wallet.disabled_time = datetime.now()
                wallet.save()
                response = {
                        'message': "Wallet Disabled",
                        'status': status.HTTP_200_OK
                    }
            else:
                response = {
                            'message': "Wallet Already Disabled",
                            'status': status.HTTP_400_BAD_REQUEST
                            }
        except Wallet.DoesNotExist:
            response = {
                        'errors': "Wallet not found!!",
                        'status': status.HTTP_400_BAD_REQUEST
                        }
        return Response(response)


class ViewWalletAPI(APIView):
    serializer_class = WalletSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response = {}
        user = self.request.user
        try:
            wallet = Wallet.objects.get(user=user)
            wallet_json = self.serializer_class(wallet).data
            wallet_json['enabled_time'] = str(wallet.enabled_time)
            response = {
                    'wallet': wallet_json,
                    'status': status.HTTP_200_OK
                }
        except Wallet.DoesNotExist:
            response = {
                        'errors': "Wallet not found!!",
                        'status': status.HTTP_400_BAD_REQUEST
                        }
        return Response(response)


class AddAmountToWalletAPI(APIView):
    serializer_class = DepositSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        response = {}
        user = self.request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data_dict = serializer.data
            reference_id = data_dict['reference_id']
            try:
                wallet = Wallet.objects.get(user=user)
                if wallet.enable == True:
                    try:
                        deposit_obj = Deposit.objects.get(reference_id=reference_id)
                        response = {
                                'errors': "Invalid reference ID!!",
                                'status': status.HTTP_400_BAD_REQUEST
                                }
                    except Deposit.DoesNotExist:
                        deposit_obj = Deposit()
                        deposit_obj.user = user
                        deposit_obj.amount = data_dict['amount']
                        deposit_obj.reference_id = reference_id
                        deposit_obj.save()
                        wallet.amount = str(int(wallet.amount)+int(deposit_obj.amount))
                        wallet.save()
                        deposit_json = {}
                        deposit_json['id'] = deposit_obj.id
                        deposit_json['user'] = deposit_obj.user.email
                        deposit_json['amount'] = deposit_obj.amount
                        deposit_json['deposit_time'] = str(deposit_obj.deposit_time)
                        deposit_json['wallet_total'] = wallet.amount
                        deposit_json['reference_id'] = deposit_obj.reference_id
                        response = {
                                'wallet': deposit_json,
                                'status': status.HTTP_200_OK
                            }
                else:
                    response = {
                            'errors': "Wallet is not enabled!!",
                            'status': status.HTTP_400_BAD_REQUEST
                            }
            except Wallet.DoesNotExist:
                response = {
                            'errors': "Wallet not found!!",
                            'status': status.HTTP_400_BAD_REQUEST
                            }
        else:
            response = {
                        'errors': serializer.errors,
                        'status': status.HTTP_400_BAD_REQUEST
                        }
        return Response(response)


