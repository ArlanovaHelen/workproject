import django_filters


class FraudFilter(django_filters.FilterSet):
    numEO = django_filters.NumberFilter(lookup_expr="iexact")
    numERDR = django_filters.NumberFilter(lookup_expr="iexact")
    card_number = django_filters.NumberFilter(lookup_expr="iexact")
    phonenumber = django_filters.NumberFilter(lookup_expr="iexact")
    district = django_filters.CharFilter(
        field_name="district__name", lookup_expr="iexact"
    )
    category = django_filters.CharFilter(
        field_name="category__name", lookup_expr="iexact"
    )

    damage__gt = django_filters.NumberFilter(field_name="damage",
                                             lookup_expr="gt")
    damage__lt = django_filters.NumberFilter(field_name="damage",
                                             lookup_expr="lt")

    date__gt = django_filters.DateFilter(field_name="date", lookup_expr="gt")
    date__lt = django_filters.DateFilter(field_name="date", lookup_expr="lt")

    victim = django_filters.CharFilter(lookup_expr="icontains")

    stage_of_crime = django_filters.BooleanFilter()

    q = django_filters.CharFilter(method="filter_by_q", label="Search")

    def filter_by_q(self, queryset, name, value):
        return (
            queryset.filter(numEO__icontains=value)
            | queryset.filter(numERDR__icontains=value)
            | queryset.filter(victim__icontains=value)
            | queryset.filter(card_number__icontains=value)
            | queryset.filter(phonenumber__icontains=value)
            | queryset.filter(category__name__icontains=value)
            | queryset.filter(district__name__icontains=value)
        )
