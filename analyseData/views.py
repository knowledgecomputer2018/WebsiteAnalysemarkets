# -*- encoding: utf-8 -*-

from django.shortcuts import render
from analyseData.models import Project
import requests
import json
from  analyseData.forms import filterForm
from payment.views import create_payment
from django.http import HttpResponseRedirect
from .symbols import symbols_nobitex
# Create your views here.

#----- real python -----------
def project_index(request):
       projects=Project.objects.all()
       context={
              'projects':projects
              }
       return render(request,'project_index.html',context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def  AnalyseData(request):
       return render(request,'index.html',{})
def telegram_index(request):
        return HttpResponseRedirect("https://web.telegram.org/z/#-542503782")
#----------------
from .scanner import  scannerMarket
def algory_index(request):         
    print('hi1')
    form = filterForm()
    # print(form)
    ResultScan=''
    filter_market=''
    config1=""
    config2=""
    if request.method == 'POST':
        form = filterForm(request.POST)
        if form.is_valid():
            print("hi2")
            filter_market=form.cleaned_data["dropDownFilter"]
            config1=float(form.cleaned_data["config1"])
            if(config2):
                   config2=float(form.cleaned_data["config2"])
              
            symbol=form.cleaned_data["symbol"]
            if(',' in symbol):
                   symbols=symbol.split(',')
                   print(symbols)
            print(filter_market,symbol,len(symbol),config1,config2)#filter_market is tuple.
            R=scannerMarket()
            if (filter_market =='PriceRange'):
                   ResultScan=R.PriceRange(config1,config2)
            elif (filter_market =='GetTradesN'):
                   print("hii")
                   ResultScan=R.get_Trades(symbol)
            elif (filter_market =='GetAllMarketsGlobalN'):
                  ResultScan=R.get_all_markets_global()
            elif (filter_market =='GetOrderbookN'):
                  ResultScan=R.get_orderbook(symbol)
            elif (filter_market =='AskSize'):
                  ResultScan=R.AskSize(config1,config2,symbol)
            elif (filter_market =='BidSize'):
                  ResultScan=R.BidSize(config1,config2,symbol)
            elif (filter_market =='BidAskRatio'):
                  ratio=config1
                  ResultScan=R.BidAskRatio(ratio)
            elif (filter_market =='AskBidRatio'):
                  ratio=config1
                  ResultScan=R.AskBidRatio(ratio)
            elif (filter_market =='Spread'):
                    spread=config1
                    ResultScan=R.Spread(spread)
            elif (filter_market =='AverageDailyVolume'):
                    ResultScan=R.AverageDailyVolume()
            elif (filter_market =='TodaysVolume'):
                    ResultScan=R.TodaysVolume(symbol,config1)
            elif (filter_market =='OneDayVolumeRatio'):
                    ResultScan=R.OneDayVolumeRatio()
            elif (filter_market =='RelativeVolumeRatio'):
                    ResultScan=R.RelativeVolumeRatio()
            elif (filter_market =='YesterdayVolumeRatio'):
                    ResultScan=R.YesterdayVolumeRatio()
                   
                   
                   
            else:
                   pass
    print('hi3')
    context = {
        'config1':config1,
        'config2':config2,
        'name':filter_market,
        'ResultScan':ResultScan,
        "form": form,
        'nobitex_symbols':symbols_nobitex ,
    }
    
    return render(request,'algory.html',context) 




#------------------
#payment crypto binance need : Merchant API
#----------------
#not work >--simple payment crypto youtube video blockonomics
def payment_crypto(request):
       payment = create_payment(
       crypto='BITCOIN', #Cryptocurrency from your settings
       fiat_amount=10, #Amount of item in fiat
       fiat_currency='USD', #Fiat currency used to convert to crypto amount
       payment_title=None,  #Title associated with payment
       payment_description=None, #Description associated with payment
       related_object=None, #Generic linked object for this payment -> crypto_payments = GenericRelation(CryptoCurrencyPayment)
       user=None, #User of this payment for non-anonymous payment
       parent_payment=None, #Associate with previous payment
       address_index=None,# Use an address generated from a particular index for this payment e.g same address can always be used for a particular user
       reuse_address=None), #Used previously paid address for this payment

       print(payment_crypto)
       return render(request,'project_index.html',{'payment_crypto':payment_crypto})

