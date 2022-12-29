from django.shortcuts import render,reverse
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("analysemarkets homepage! ")

base_url = "https://api.nobitex.ir/"
VERSION2="v2/"
def get_Trades(request,symbol):#general
    
    Trades_url = base_url+VERSION2+"trades/"+symbol

    payload = ""
    headers = {}

    response = requests.request("GET", Trades_url, headers=headers, data=payload)
    result=json.loads(response.text)
    print(result)
    if(result['status']== 'ok'):
        latestTrades=result["trades"][-8:]
       
        return render(request,'index.html',{'trades':trades})
