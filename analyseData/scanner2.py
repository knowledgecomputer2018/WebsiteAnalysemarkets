#-------------------- Nobitex Exchange ------------------------
base_url = "https://api.nobitex.ir/"
VERSION2="v2/"
symbol='BTCIRT'

def get_token(request):
     #errors :'non_field_errors': ['OTP not provided'], 'code': 'MissingOTP'} >>>2FA
     # X-TOTP:?

    user='knowledgecomputer2018@gmail.com'
    psw='LpA3ma$d6LgEPQm'
    login_url=base_url+"auth/login/"

    payload = json.dumps({
      " username": user,
      "password":psw,
      'captcha':'api'
    })
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", login_url, headers=headers, data=payload)
    #output response is str then convert str to json .
    
    result=(json.loads(response.text))
    print(result)
    if(result):
       return render(request,'index.html',{'token':result,'sym':symbol})
    
#def get_Trades(request,symbol):#general
def get_Trades(request):#general
    Trades_url = base_url+VERSION2+"trades/"+symbol

    payload = ""
    headers = {}

    response = requests.request("GET", Trades_url, headers=headers, data=payload)
    result=json.loads(response.text)
    print(result)
    if(result['status']== 'ok'):
        trades=result["trades"][-8:]
       
        return render(request,'index.html',{'trades':trades,'sym':symbol})
def get_all_markets_global(request):
    markets_url = base_url+"market/global-stats"

    payload = ""
    headers = {}

    all_markets=[]
    response = requests.request("POST", markets_url, headers=headers, data=payload)
    markets=json.loads(response.text)
    print(type(markets['markets']))
    if(markets['status']=='ok'):
        return render(request,'index.html',{'markets':markets['markets'],'sym':symbol})
def get_OHCL(request):
    ohcl_url=markets_url = base_url+"/market/udf/history?symbol="+symbol+"&resolution=D&from=1562058167&to=1562230967"
    payload = ""
    headers = {}

    ohcl={}
    response = requests.request("GET", markets_url, headers=headers, data=payload)
    ohcl_nob=json.loads(response.text)
    #t': [1562095800, 1562182200], 'o': [146272500.0, 150551000.0], 'h': [155869600.0, 161869500.0], 'l': [140062400.0, 150551000.0], 'c': [151440200.0, 157000000.0], 'v': [18.221362316, 9.8592626506]}
    ohcl={'time':ohcl_nob['t'],'open':ohcl_nob['o'],'high':ohcl_nob['h'],'low':ohcl_nob['l'],'close':ohcl_nob['c'],'volume':ohcl_nob['v']}
    
    print("HI")
    print(ohcl)
    if(ohcl_nob['s']=='ok'):
           return render(request,'index.html',{'ohcl':ohcl,'sym':symbol})
def get_orderbook(request):#general
#def get_orderbook(symbol):#general
    
    orderbook_url = base_url+VERSION2+"orderbook/"+symbol

    payload = ""
    headers = {}

    response = requests.request("GET", orderbook_url, headers=headers, data=payload)
    result=json.loads(response.text)
    print(result)
    if(result['status']=='ok'):
        orderbook=[]
        ask=result['asks'][-8:]
        bid=result['bids'][-8:]
        orderbook.append({'asks':ask,'bids':bid})
        return render(request,'index.html',{'ordersbook':orderbook,'sym':symbol}) #!
def get_depthorders(request):#general
    orderbook_url = base_url+VERSION2+"depth/"+symbol
    payload = ""
    headers = {}
    response = requests.request("GET", orderbook_url, headers=headers, data=payload)
    depthorders=json.loads(response.text)
    print(depthorders)
    if(depthorders['status']=='ok'):
        return render(request,'index.html',{'depthorders':depthorders,'sym':symbol})
       


#-------------------- Binance Exchange ------------------------

#ValueError: source code string cannot contain null bytes
#from binance.enums import *
#from binance.client import Client
#from binance.exceptions import BinanceAPIException,BinanceOrderException
       
name_loggfile="log_app.txt"
def write_log(text):
    f=open(name_loggfile,'a')#append text
    write_logfie=f.write(text+" \n")
    #f.write("\n")
    f.close()
with open("Accounts.json", "r") as read_file:
     Accounts = json.load(read_file)

def get_Accounts():#create client binance from accounts 
    clients=[]
    for Account in Accounts.values():
        flag=Account['flag']
        print(flag)
        if(flag):
            person=Account['name']
            write_log("account is active:{}".format(person))
            print("account is active:{}".format(person))
            API_KEY=Account['API_KEY']
            SECRET_KEY=Account['SECRET_KEY']
            client = Client(API_KEY,SECRET_KEY)
            clients.append(client)
    write_log("number accounts is:{}".format(len(clients)))
    if (len(clients)== 0):
        print("accounts is empty.")
    return clients
#def get_klines(client,TRADE_SYMBOL,candle_type):
def get_klines(request):
    symbol='BTCUSDT'
    candle_type='5m'
    #binance.exceptions.BinanceAPIException: APIError(code=-1121): Invalid symbol.

    #client=get_Accounts()[0]
    #klines=client.get_historical_klines(TRADE_SYMBOL,candle_type,datetime.now().strftime("%m/%d/%Y"))#13previous candle(historical) +get candle now(socket)
    #active accounts
    clients=get_Accounts()
    client=clients[0]
    klines=client.get_historical_klines(symbol,candle_type,"2 day ago UTC")#13previous candle(historical) +get candle now(socket)
    #print(len(klines))
    #print(klines[4],klines[6])#last candle 13:45 if time now :13:47
   
    '''
    [
                    1499040000000,      # Open time
                    "0.01634790",       # Open
                    "0.80000000",       # High
                    "0.01575800",       # Low
                    "0.01577100",       # Close
                    "148976.11427815",  # Volume
                    1499644799999,      # Close time
                    "2434.19055334",    # Quote asset volume
                    308,                # Number of trades
                    "1756.87402397",    # Taker buy base asset volume
                    "28.46694368",      # Taker buy quote asset volume
                    "17928899.62484339" # Can be ignored
                ]
    '''
    return klines #klines type is list.
    print(klines)
 
    return render(request,'index.html',{'candles':klines,'sym':symbol})
