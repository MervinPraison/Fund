from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import data_fund, data_fund_investment, data_call, data_commitment

def index(request):
    latest_fund_list = data_fund.objects.order_by('fund_id')[:5]
    data_calls = data_call.objects.all() # optimizing
    template = loader.get_template('funding/index.html')
    context = {
        'latest_fund_list': latest_fund_list,
        'data_calls': data_calls,
    }
    return HttpResponse(template.render(context, request))

def detail(request, fund_id):
    fund = get_object_or_404(data_fund, pk=fund_id)
    return render(request, 'funding/detail.html', {'fund': fund})

def newcall(request):
    latest_commitment_list = data_commitment.objects.order_by('commitment_id')[:100]
    data_fund_investment_list = data_fund_investment.objects.order_by('id')[:100]
    dfi = data_fund_investment.objects.select_related('commitment_id')
    template = loader.get_template('funding/newcall.html')
    context = {
        'latest_commitment_list': latest_commitment_list,
        'data_fund_investment_list': data_fund_investment_list,
        'dfi': dfi
    }
    return HttpResponse(template.render(context, request))
