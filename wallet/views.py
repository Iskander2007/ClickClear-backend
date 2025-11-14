from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, response
from .models import Transaction, TxType, TxStatus

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def deposit(request):
    # Мок-пополнение: просто увеличиваем баланс (для dev)
    amount = round(float(request.data.get("amount", 0)), 2)
    if amount < 100: return response.Response({"detail":"Минимум 100 ₸"}, status=400)
    user = request.user
    user.balance += amount; user.save()
    Transaction.objects.create(user=user, type=TxType.DEPOSIT, amount=amount, status=TxStatus.SUCCESS)
    return response.Response({"balance": str(user.balance)})

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def withdraw(request):
    amount = round(float(request.data.get("amount", 0)), 2)
    if amount < 100: return response.Response({"detail":"Минимум 100 ₸"}, status=400)
    user = request.user
    if user.balance < amount: return response.Response({"detail":"Недостаточно средств"}, status=400)
    user.balance -= amount; user.save()
    Transaction.objects.create(user=user, type=TxType.WITHDRAW, amount=amount, status=TxStatus.PENDING)
    return response.Response({"balance": str(user.balance), "status":"pending"})
