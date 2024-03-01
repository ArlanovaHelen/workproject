from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from frauds.serializers import (
    FraudSerializer,
    CategoryWithFraudsSerializer,
    FraudViewSerializer,
    CategorySerializer,
    DistrictSerializer,
    DistrictWithFraudsSerializer,
    PrisonSerializer,
    PhonenumberFileSerializer,
    PhonenumberViewSerializer,
)
from frauds.models.fraud import Fraud
from frauds.models.category import Category
from frauds.models.district import District
from frauds.models.prison import Prison
from frauds.models.num_file import PhonenumberFile
# from frauds.permissions import MyCustomPermission
from django_filters.rest_framework import DjangoFilterBackend
from frauds.filters import FraudFilter
from rest_framework.filters import OrderingFilter


from workproject.authentication import MyCustomAuthentication


class FraudViewSet(ModelViewSet):
    queryset = Fraud.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = FraudFilter
    ordering_fields = ("category", "numEO")
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return FraudViewSerializer
        else:
            return FraudSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.filter(user=self.request.user)

#    authentication_classes = (IsAuthenticated,)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().prefetch_related("frauds")
    serializer_class = CategoryWithFraudsSerializer

    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CategoryWithFraudsSerializer
        else:
            return CategorySerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.filter(user=self.request.user)


class DistrictViewSet(ModelViewSet):
    queryset = District.objects.all().prefetch_related("frauds")
    serializer_class = DistrictWithFraudsSerializer

    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DistrictWithFraudsSerializer
        else:
            return DistrictSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.filter(user=self.request.user)


class PrisonViewSet(ModelViewSet):
    queryset = Prison.objects.all()
    serializer_class = PrisonSerializer

    permission_classes = (IsAuthenticated,)


class PhonenumberFileViewSet(ModelViewSet):
    queryset = PhonenumberFile.objects.all()
    serializer_class = PhonenumberFileSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PhonenumberViewSerializer
        else:
            return PhonenumberFileSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset.all()
        else:
            return None
