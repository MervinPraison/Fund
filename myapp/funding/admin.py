from django.contrib import admin

from .models import data_fund, data_commitment, data_call, data_fund_investment

admin.site.register(data_fund)
admin.site.register(data_commitment)
admin.site.register(data_call)
admin.site.register(data_fund_investment)