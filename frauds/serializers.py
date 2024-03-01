from rest_framework import serializers
from frauds.models.fraud import Fraud
from frauds.models.category import Category
from frauds.models.district import District
from frauds.models.prison import Prison
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from frauds.tasks import fraud_created_task
from frauds.parsing_history_number import read_file_task
from frauds.models.num_file import PhonenumberFile


class PhonenumberFileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PhonenumberFile
        fields = ("name", "data", "user")

    def create(self, validated_data):
        phonenumber_file = PhonenumberFile.objects.create(**validated_data)

        read_file_task.delay(
            name_file=rf"/home/lena/WorkProjectFrauds/WorkProject/num_history/{phonenumber_file.name}"
        )

        return phonenumber_file


class PhonenumberViewSerializer(PhonenumberFileSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ("name", "oblast")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class FraudSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Fraud
        fields = (
            "id",
            "numEO",
            "date",
            "district",
            "category",
            "victim",
            "numERDR",
            "card_number",
            "phonenumber",
            "phonenumber_location",
            "phonenumber_history",
            "damage",
            "stage_of_crime",
            "user",
        )

    def create(self, validated_data):
        #        order_products = validated_data.pop("order_products")
        fraud = Fraud.objects.create(**validated_data)

        fraud_created_task.delay(fraud.numEO)

        return fraud


class FraudViewSerializer(FraudSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = CategorySerializer()


class CategoryWithFraudsSerializer(CategorySerializer):
    frauds = FraudSerializer(many=True)

    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields + ("frauds",)


class DistrictWithFraudsSerializer(DistrictSerializer):
    frauds = FraudSerializer(many=True)

    class Meta(DistrictSerializer.Meta):
        fields = DistrictSerializer.Meta.fields + ("frauds",)


class PrisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prison
        fields = ("name", "lat", "lon", "address", "oblast")


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, user):
        token, _ = Token.objects.get_or_create(user=user)
        return token.key

    class Meta:
        model = User
        fields = ("username", "password", "email",
                  "first_name", "last_name", "token")
