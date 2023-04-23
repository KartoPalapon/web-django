from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app_general.forms import SubscriptionModelForm

# Create your views here.

def index(request):
    return render(request, 'app_general/index.html')

def about(request):
    return render(request, 'app_general/about.html')

def feature(request):
    return render(request, 'app_general/feature.html')




def subscription(request):
    # POST
    if request.method == 'POST':
        form = SubscriptionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subscription_thankyou'))
    else:
        form = SubscriptionModelForm()
    
    # GET
    context = {'form': form}
    return render(request, 'app_general/nouse/subscription_form.html', context)

def subscription_thankyou(request):
    return render(request, 'app_general/subscription_thankyou.html')
    