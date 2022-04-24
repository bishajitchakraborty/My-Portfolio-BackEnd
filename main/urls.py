from django.urls import include, path
from rest_framework.routers import DefaultRouter

from main import views

router = DefaultRouter()
router.register("home", views.HomeApi, basename='Home')
router.register("about", views.AboutApi, basename='About')
router.register("contact", views.ContactApi, basename='Contact')
router.register("message", views.MessageApi, basename='Message')
router.register("service", views.ServiceApi, basename='Service')
router.register("work-process", views.WorkProcessApi, basename='WorkProcess')
router.register("portfolio", views.PortfolioApi, basename='Portfolio')

urlpatterns = [
    path('',include(router.urls))
]