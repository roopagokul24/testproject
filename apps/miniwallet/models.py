from django.db import models

# Create your models here.

class Wallet(models.Model):
    user = models.ForeignKey(
                            'account.CustomUser',
                            related_name='wallet_owner',
                            null=True, on_delete=models.CASCADE,
                            db_index=True
                            )
    amount = models.CharField(max_length=15, verbose_name="Amount")
    enable = models.BooleanField(default=False)
    enabled_time = models.DateTimeField(verbose_name='Enabled Time',
                                        null=True, blank=True,
                                        default=None)
    disabled_time = models.DateTimeField(verbose_name='Disabled Time',
                                        null=True, blank=True,
                                        default=None)

    def __str__(self):
        return self.user.email


class Deposit(models.Model):
    user = models.ForeignKey(
                            'account.CustomUser',
                            related_name='wallet_owner_deposit',
                            null=True, on_delete=models.CASCADE,
                            db_index=True
                            )
    amount = models.CharField(max_length=15, verbose_name="Amount")
    reference_id = models.CharField(max_length=15, verbose_name="Amount",
                                    null=True, blank=True)
    deposit_time = models.DateTimeField(verbose_name='Created Time',
                                        auto_now_add=True)

    def __str__(self):
        return self.user.email


class Withdrawal(models.Model):
    user = models.ForeignKey(
                            'account.CustomUser',
                            related_name='wallet_owner_withdrawal',
                            null=True, on_delete=models.CASCADE,
                            db_index=True
                            )
    amount = models.CharField(max_length=15, verbose_name="Amount")
    reference_id = models.CharField(max_length=15, verbose_name="Amount",
                                    null=True, blank=True)
    withdrawal_time = models.DateTimeField(verbose_name='Created Time',
                                        auto_now_add=True)

    def __str__(self):
        return self.user.email