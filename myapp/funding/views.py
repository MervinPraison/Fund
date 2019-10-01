from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import data_fund

def index(request):
    latest_fund_list = data_fund.objects.order_by('fund_id')[:5]
    template = loader.get_template('funding/index.html')
    context = {
        'latest_fund_list': latest_fund_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, fund_id):
    fund = get_object_or_404(data_fund, pk=fund_id)
    return render(request, 'funding/detail.html', {'fund': fund})