"""
URL configuration for workproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from graphene_django.views import GraphQLView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt

# from rest_framework.authtoken.views import obtain_auth_token
from frauds.viewsets import (
    FraudViewSet,
    CategoryViewSet,
    DistrictViewSet,
    PrisonViewSet,
    PhonenumberFileViewSet,
)

router = DefaultRouter()
router.register("frauds", FraudViewSet)
router.register("categories", CategoryViewSet)
router.register("districts", DistrictViewSet)
router.register("prisons", PrisonViewSet)
router.register("phonenumber", PhonenumberFileViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Frauds API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/auth/', obtain_auth_token),
    path("api/", include(router.urls)),
    path('api/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
