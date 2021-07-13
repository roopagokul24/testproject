from django.urls import path
from .views import InitializeWalletAPI, EnableWalletAPI, ViewWalletAPI, \
                   AddAmountToWalletAPI, UseAmountFromWalletAPI, \
                   DisableWalletAPI

urlpatterns = [
    path('init/', InitializeWalletAPI.as_view(), name="init"),
    path('enable-wallet/', EnableWalletAPI.as_view(), name="enable-wallet"),
    path('view-wallet/', ViewWalletAPI.as_view(), name="view-wallet"),
    path('wallet/deposit/', AddAmountToWalletAPI.as_view(), name="add-to-wallet"),
    path('wallet/withdraw/', UseAmountFromWalletAPI.as_view(), name="withdraw-from-wallet"),
    path('disable-wallet/', DisableWalletAPI.as_view(), name="disable-wallet"),
]