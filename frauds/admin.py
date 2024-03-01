from django.contrib import admin
from frauds.models.fraud import Fraud
from frauds.models.category import Category
from frauds.models.district import District
from frauds.models.prison import Prison
from frauds.models.imei_history import Imei
from frauds.models.phonenumber_history import Phonenumber
from frauds.models.num_file import PhonenumberFile
from frauds.models.control import Control
from frauds.models.bs_location import BSLocation


admin.site.register(Fraud)
admin.site.register(Category)
admin.site.register(District)
admin.site.register(Prison)
admin.site.register(Imei)
admin.site.register(Phonenumber)
admin.site.register(PhonenumberFile)
admin.site.register(Control)
admin.site.register(BSLocation)


# Register your models here.
