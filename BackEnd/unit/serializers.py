from rest_framework import serializers
from unit.models import (
    CommonZone,
    ZoneRequest,
    HousingType,
    Nomenclature,
    HousingUnit,
    HabitantDetail,
)


class CommonZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonZone
        fields = "__all__"


class ZoneRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneRequest
        fields = "__all__"


class HousingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingType
        fields = "__all__"


class NomenclatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomenclature
        fields = "__all__"


class HousingUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingUnit
        fields = "__all__"


class HabitantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitantDetail
        fields = "__all__"
