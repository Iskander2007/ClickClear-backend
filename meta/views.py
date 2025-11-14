from rest_framework import generics, response, permissions
from rest_framework.decorators import api_view, permission_classes   # ← добавить
from .models import District, Slot
from .serializers import DistrictSerializer

class DistrictList(generics.ListAPIView):
    queryset = District.objects.all().order_by("name")
    serializer_class = DistrictSerializer

@api_view(["GET"])                                # ← добавить
@permission_classes([permissions.AllowAny])       # ← можно и не добавлять, но явно лучше
def slots_list(request):
    data = [{"value": c.value, "label": c.label} for c in Slot]
    return response.Response(data)
