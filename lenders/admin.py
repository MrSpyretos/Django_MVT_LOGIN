from django.contrib import admin
from .models import Lender
# Register your models here.

class LenderAdmin(admin.ModelAdmin):
    fields=["Class",
            "Installments",
            "Amount",
            "Duration"]
admin.site.register(Lender , LenderAdmin)