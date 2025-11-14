from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, response
from accounts.views import RegisterView, login_view, logout_view, me, verify_email
from meta.views import DistrictList, slots_list
from orders.views import OrdersFeed, MyOrdersClient, CreateOrder, take_order, cancel_order, mark_failed, complete_order
from wallet.views import deposit, withdraw


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def health(_):
    return response.Response({"ok": True})


def root(_):
    return JsonResponse({"service": "Click&Clean API", "status": "ok"})

urlpatterns = [
    path("", root),
    path("admin/", admin.site.urls),
    path("api/health", health),

    # auth
    path("api/auth/register", RegisterView.as_view()),
    path("api/auth/login", login_view),
    path("api/auth/logout", logout_view),
    path("api/auth/me", me),
    path("api/auth/verify-email", verify_email),

    # meta
    path("api/meta/districts", DistrictList.as_view()),
    path("api/meta/slots", slots_list),

    # orders
    path("api/orders", OrdersFeed.as_view()),                # лента (курьеры)
    path("api/my/orders", MyOrdersClient.as_view()),         # мои (клиент)
    path("api/orders/create", CreateOrder.as_view()),        # создать (клиент)
    path("api/orders/<int:pk>/take", take_order),            # взять (курьер)
    path("api/orders/<int:pk>/cancel", cancel_order),        # отменить
    path("api/orders/<int:pk>/failed", mark_failed),         # не удалось
    path("api/orders/<int:pk>/complete", complete_order),    # завершить

    # wallet
    path("api/wallet/deposit", deposit),
    path("api/wallet/withdraw", withdraw),
]
