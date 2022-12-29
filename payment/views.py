import requests
from django.shortcuts import render,reverse
from .models import *
import uuid
from analysemarkets import settings
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
       print('hi')
       products=Product.objects.all()
       print(products)
       return render(request,'product.html',context={'products':products})
def exchanged_rate(amount):
       url='blockonomics.co/api/price?currency=USD'
       r=requests.get(url,params=params)
       response=r.json()
       return amount/response['price']
def track_invoice(request,pk):
       invoice_id=pk
       invoice=Invoice.objects.get(id=invoice_id)
       data={
              'order_id':invoice.order_id,
              'bits':invoice.btcvalue/1e8,
              'value':invoice.product.price,
              'addr':invoice.address,
              'status':Invoice.STATUS_CHOICES[invoice.status+1][1],
              'invoice_status':invoice.status,
              }
       print(invoice.recieved)
       if (invoice.recieved):
              data['paid']=invoice.recieved/1e8
              if(int(invoice.btcvalue)<=int(invoice.received)):
                     data['path']=invoice.product.product_image.url

       else:
              data['paid']=0
       return render(request,'invoice.html',context=data)
       
       
def create_payment(request,pk):
       
       print('pk:%s' %pk)
       product_id=pk
       #Product model or connect to sqlite database.
       product=Product.objects.get(id=product_id)
       print(product)
       #argument:xpub
       url='https://www.blockonomics.co/api/new_address'
       print(settings.API_KEY)
       headers={'Authorization':'Bearer'+settings.API_KEY}
       r=requests.post(url,headers=headers)
       print(r.json)
       if r.status_code==200:
              address=r.json()['address']
              bits=exchanged_rate(product.price)
              # helps in generating random objects of 128 bits as ids
              order_id=uuid.uuid1()
              invoice=Invoice.objects.create(order_id=order_id,address=address,btcvalue=bits*1e8,product=product)
              
              # using the named URL(urls.py name="")
              #If the URL accepts arguments, you may pass them in args.You can also pass kwargs instead of args.
              return HttpResponseRedirect(reverse('track_payment',kwargs={'pk':invoice.id}))
       else:
              print(r.status_code,r.text)
              return HttpResponse("Some Error,Try Again!")
       
def receive_payment(request):
    
    if (request.method != 'GET'):
        return 
    
    txid  = request.GET.get('txid')
    value = request.GET.get('value')
    status = request.GET.get('status')
    addr = request.GET.get('addr')

    invoice = Invoice.objects.get(address = addr)
    
    invoice.status = int(status)
    if (int(status) == 2):
        invoice.received = value
    invoice.txid = txid
    invoice.save()
    return HttpResponse(200)

#-------------------
#-------------------
#-------------------
#-------------------



def binance_payment():
       #must be 32 digits
       #A random string with 32 bytes, e.g. random ascii decimal within a-z and A-Z and loop 32 times to form a random string
       nonce=random_string()
       
       #Binance pay only process request within 1s
       #UnixTimestamp in milliseconds that the requests send, guarantee the machine time is sync with the network
       timestamp = get_timestamp()

       #?
       request={
             "env" :{
             "terminalType" : "APP" 
          }, 
       "merchantTradeNo": rand(982538,9825382937292), 
       "orderAmount" : 25.17, 
       "currency" : "USDT", 
       "goods" : {
                "goodsType" : "01", 
                "goodsCategory" : "D000", 
                "referenceGoodsId": "7876763A3B", 
                "goodsName" :"Ice Cream", 
                "goodsDetail": "Greentea ice cream cone" 
             }
       }
       json_request=json.dumps(json)
       
       payload = timestamp+"\n".nonce+"\n"+json_request+"\n";

       binance_pay_key = "REPLACE-WITH-YOUR-BINANCE-MERCHANT-API-KEY";
       binance_pay_secret = "REPLACE-WITH-YOUR-BINANCE-MERCHANT-API-SECRETE-KEY";

       signature = strtoupper(hash_hmac('SHA512',payload,binance_pay_secret));

       headers = {
           "Content-Type":" application/json",
           "BinancePay-Timestamp": timestamp,
            "BinancePay-Nonce":nonce,
            "BinancePay-Certificate-SN":binance_pay_key,
            "BinancePay-Signature":signature,
            }
       
       base_url='https://bpay.binanceapi.com/'
       url=base_url+"binancepay/openapi/v2/order"
       RETURNTRANSFER='1'
       
       response=requests.post(json_request,headers=headers)
       
       
