from . import views
from django.db import router
from django.urls import path
from rest_framework import routers

# upload file xlsx to add to database

router = routers.SimpleRouter()
router.register('energycosts', views.EnergyCostViewSet)
router.register('energycompany', views.EnergyTradingCompanyViewSet)
urlpatterns = router.urls + [
    path("energycosts/upload/<str:filename>/", views.UploadXlsx.as_view()),
]