import graphene
from frauds.models import Fraud
from frauds.models import District
from frauds.models import Category
from frauds.models import Prison
from graphene_django import DjangoObjectType
class FraudType(DjangoObjectType):
    class Meta:
        model = Fraud

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class DistrictType(DjangoObjectType):
    class Meta:
        model = District

class PrisonType(DjangoObjectType):
    class Meta:
        model = Prison

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi")
    all_frauds = graphene.List(FraudType)
    all_categories = graphene.List(CategoryType)
    all_districts = graphene.List(DistrictType)
    all_prisons = graphene.List(PrisonType)

    def resolve_all_frauds(self, info):
        return Fraud.objects.all()

    def resolve_all_categories(self, info):
        return Category.objects.all()

    def resolve_all_districts(self, info):
        return District.objects.all()

    def resolve_all_prisons(self, info):
        return Prison.objects.all()





schema = graphene.Schema(query=Query)

