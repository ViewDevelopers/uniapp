from rest_framework import viewsets
from rest_framework import permissions
from unit.models import (
    CommonZone,
    ZoneRequest,
    HousingType,
    Nomenclature,
    HousingUnit,
    HabitantDetail,
)
from .serializers import (
    CommonZoneSerializer,
    ZoneRequestSerializer,
    HousingTypeSerializer,
    NomenclatureSerializer,
    HousingUnitSerializer,
    HabitantDetailSerializer,
)


class CommonZoneViewSet(viewsets.ModelViewSet):
    queryset = CommonZone.objects.all()
    serializer_class = CommonZoneSerializer
    permission_classes = [permissions.AllowAny]


class ZoneRequestViewSet(viewsets.ModelViewSet):
    queryset = ZoneRequest.objects.all()
    serializer_class = ZoneRequestSerializer
    permission_classes = [permissions.AllowAny]


class HousingTypeViewSet(viewsets.ModelViewSet):
    queryset = HousingType.objects.all()
    serializer_class = HousingTypeSerializer
    permission_classes = [permissions.AllowAny]


class NomenclatureViewSet(viewsets.ModelViewSet):
    queryset = Nomenclature.objects.all()
    serializer_class = NomenclatureSerializer
    permission_classes = [permissions.AllowAny]


class HousingUnitViewSet(viewsets.ModelViewSet):
    queryset = HousingUnit.objects.all()
    serializer_class = HousingUnitSerializer
    permission_classes = [permissions.AllowAny]


class HabitantDetailViewSet(viewsets.ModelViewSet):
    queryset = HabitantDetail.objects.all()
    serializer_class = HabitantDetailSerializer
    permission_classes = [permissions.AllowAny]
