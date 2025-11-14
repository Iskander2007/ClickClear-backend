from django.db import models
from django.conf import settings

class TxType(models.TextChoices):
    DEPOSIT="deposit","Пополнение"
    WITHDRAW="withdraw","Вывод"
    HOLD="hold","Резерв"
    RELEASE="release","Списание в пользу курьера"
    REFUND="refund","Возврат"

class TxStatus(models.TextChoices):
    PENDING="pending","Ожидает"
    SUCCESS="success","Успех"
    FAILED="failed","Ошибка"

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TxType.choices)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=10, choices=TxStatus.choices, default=TxStatus.SUCCESS)
    related_order_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
