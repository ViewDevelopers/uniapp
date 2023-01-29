from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from user.views import UserViewSet, AdminAccountViewSet, UserTypeViewSet, IDTypeViewSet
from polls.views import PeriodViewSet, PositionViewSet, CandidateViewSet, PollViewSet
from unit.views import (
    CommonZoneViewSet,
    ZoneRequestViewSet,
    HousingTypeViewSet,
    NomenclatureViewSet,
    HousingUnitViewSet,
    HabitantDetailViewSet,
)

router = routers.DefaultRouter()

router.register(r"user/users", UserViewSet)
router.register(r"user/admin", AdminAccountViewSet)
router.register(r"user/usertype", UserTypeViewSet)
router.register(r"user/idtype", IDTypeViewSet)
router.register(r"polls/period", PeriodViewSet)
router.register(r"polls/position", PositionViewSet)
router.register(r"polls/candidate", CandidateViewSet)
router.register(r"polls/poll", PollViewSet)
router.register(r"unit/commonzone", CommonZoneViewSet)
router.register(r"unit/zonerequest", ZoneRequestViewSet)
router.register(r"unit/housingtype", HousingTypeViewSet)
router.register(r"unit/nomenclature", NomenclatureViewSet)
router.register(r"unit/housingunit", HousingUnitViewSet)
router.register(r"unit/habitantdetail", HabitantDetailViewSet)

urlpatterns = [
    # djoser
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.social.urls")),
    # restframework
    path("", include(router.urls)),
    # api con Apiview, descomente para utilizar
    # path("api/users/", include("user.urls")),
    # django
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Para conectar con las urls de React
urlpatterns += [re_path(r"^.*", TemplateView.as_view(template_name="index.html"))]
