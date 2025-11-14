from .models import Order, OrderStatus
from django.db.models import Q

def filter_orders(qs, params, user=None):
    # показываем только NEW (ленту для курьеров)
    qs = qs.filter(status=OrderStatus.NEW)
    if "district" in params: qs = qs.filter(district_id__in=params.get("district").split(","))
    if "min_amount" in params: qs = qs.filter(amount__gte=params.get("min_amount"))
    if "max_amount" in params: qs = qs.filter(amount__lte=params.get("max_amount"))
    if "date" in params: qs = qs.filter(date=params["date"])
    if "slot" in params: qs = qs.filter(slot=params["slot"])
    return qs
