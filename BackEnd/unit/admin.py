from django.contrib import admin
from unit.models import (
    CommonZone,
    Nomenclature,
    HabitantDetail,
    HousingType,
    HousingUnit,
)

admin.site.register(CommonZone)
admin.site.register(Nomenclature)
admin.site.register(HabitantDetail)
admin.site.register(HousingType)
admin.site.register(HousingUnit)
