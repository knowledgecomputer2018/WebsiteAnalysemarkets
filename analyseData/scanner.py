
from binance import Client
import json,requests
from .unixDateTime import milliseconds_to_date,epoch_to_datetime,datetime_to_epoch
from datetime import datetime,timedelta
from .symbols import symbols_nobitex
from time import sleep,time

with open("Accounts.json", "r") as read_file:
     Account = json.load(read_file)

#algory website
class scannerMarket():
       def __init__(self):
              #binance error :max retry
              flag=Account['1']['flag']
              if(flag):        
                     API_KEY=Account['1']['API_KEY']
                     SECRET_KEY=Account['1']['SECRET_KEY']
                     print('declare client')
                     #self.client=Client(API_KEY,SECRET_KEY)

               #----------------------------------------
              self.base_url = "https://api.nobitex.ir/"
              self.VERSION2="v2/"
              #self.symbol='BTCUSDT'
       
       #----------------------------------------------functions Nobitex
       def get_Trades(self,symbol):#general
           
           Trades_url = self.base_url+self.VERSION2+"trades/"+symbol

           payload = ""
           headers = {}

           response = requests.request("GET", Trades_url, headers=headers, data=payload)
           result=json.loads(response.text)
           #print(result)
           if(result['status']== 'ok'):
               #trades=result["trades"][-8:]
               #change unix time to datetime
               #print(trades)
               list_trades=[]
               for key in result['trades']:
                      list_trades.append({'time':milliseconds_to_date(key['time']),'price': key['price'], 'volume': key['volume'], 'type': key['type']} )                           
               return list_trades
       def get_all_markets_global(self):
           markets_url = self.base_url+"market/global-stats"

           payload = ""
           headers = {}

           all_markets=[]
           response = requests.request("POST", markets_url, headers=headers, data=payload)
           markets=json.loads(response.text)
           #print((markets['markets']))
           if(markets['status']=='ok'):
                  return markets['markets']['binance']
       def get_orderbook(self,symbol):#general
           orderbook_url = self.base_url+self.VERSION2+"orderbook/"+symbol           
            #orderbook_url = self.base_url+self.VERSION2+"orderbook/all"

           payload = ""
           headers = {}

           response = requests.request("GET", orderbook_url, headers=headers, data=payload)
           result=json.loads(response.text)

           dic_orderbook={}
           if(result['status']=='ok'):
              
              if(symbol !='all'):
                     lastUpdate=milliseconds_to_date(result['lastUpdate'])
                     #lastTradePrice=result['lastTradePrice']
                     #asks=result['asks']
                     #bids=result['bids']
                     dic_orderbook={'lastUpdate':lastUpdate,'lastTradePrice':result['lastTradePrice'],'asks':result['asks'],'bids':result['bids']}
                     return dic_orderbook
              return result
               
           else:
                 print(result)
                 return None
       
       def get_OHCL_N(self,symbol,candle_type,frm,to):
           ohcl_url=self.base_url+"/market/udf/history?symbol="+symbol+"&resolution="+candle_type+"&from="+frm+"&to="+to
           print(ohcl_url)
           payload = ""
           headers = {}

           ohcl={}
           tm_datetime=[]
           response = requests.request("GET", ohcl_url, headers=headers, data=payload)
           ohcl_nob=json.loads(response.text)
           print(ohcl_nob)
           if (ohcl_nob['s']=='ok'):
                         #t': [1562095800, 1562182200], 'o': [146272500.0, 150551000.0], 'h': [155869600.0, 161869500.0], 'l': [140062400.0, 150551000.0], 'c': [151440200.0, 157000000.0], 'v': [18.221362316, 9.8592626506]}
                         for i in  range(len(ohcl_nob['t'])):
                               tm_datetime.append({'time':epoch_to_datetime(ohcl_nob['t'][i]),'open':ohcl_nob['o'][i],'high':ohcl_nob['h'][i],'low':ohcl_nob['l'][i],'close':ohcl_nob['c'][i],'volume':ohcl_nob['v'][i]})
                         ohcl[symbol]=tm_datetime
                         
                         print("HI")
                         print(ohcl)          
                         return ohcl
           else:
                    return ohcl_nob
       #----------------------------------------------functions algory 
       def PriceRange(self,config1,config2):#1
              print('hi Price range')
              markets_dic={}
              markets=self.get_all_markets_global()
              print(markets['binance']['mkr'])
              for market in markets['binance']:
                     if(markets['binance'][market]>config1 and markets['binance'][market]<config2):
                            print(market,markets['binance'][market])
                            markets_dic[market]=markets['binance'][market]
              #get_symbols_price=self.client.get_exchange_info()
              #get_symbol_price=self.client.get_symbol_info('ADAUSDT')
              #return  get_symbol_price
              return markets_dic
       def AskSize(self,config1,config2,symbol):#2
              Asks={}
              PriceAsk_list=[]
              asks_list=[]
              #print("Num symbols:{}".format(len(symbols_nobitex)))
              #for symbol in symbols_nobitex:
                #     print(symbol)
              #value=self.get_orderbook('all')
              value=self.get_orderbook(symbol)
              
              if(value):
                     #Asks.update({symbol:value['asks']})
                     #sleep(0.1)
                  #for sym in symbols_nobitex:
                     print(symbol)
                     #if(value[symbol]):
                            #all
                            #lastUpdate=value[symbol]['lastUpdate']
                            #lastTradePrice=value[symbol]['lastTradePrice']
                     lastUpdate=value['lastUpdate']
                     lastTradePrice=value['lastTradePrice']
                     asks=value['asks']
                     print("lastUpdate:{} ,lastTradePrice:{}".format(lastUpdate,lastTradePrice))
                     #all
                     #asks=value[symbol]['asks']
                     print("asks:\n price      ask")
                     for price,ask in asks:#key:price,val:ask
                            asks_list.append(ask)
                            if(float(ask)>config1 and float(ask)<config2):
                                   print(price,ask)
                                   PriceAsk_list.append({"price":price,"ask":ask})
                     Asks.update({symbol:PriceAsk_list,"lastUpdate":lastUpdate,'lastTradePrice':lastTradePrice})
                     print(len(Asks))
                     if(len(PriceAsk_list)==0):
                            min_ask=min(asks_list)
                            max_ask=max(asks_list)
                            Asks.update({symbol:{"min_ask":min_ask,"max_ask":max_ask}})
              return Asks

               #get_Asks=client.get_order_book()
#               DepthCache.get_asks()
       def BidSize(self,config1,config2,symbol):#3
              Bids={}
              PriceBid_list=[]
              bids_list=[]
              #print("Num symbols:{}".format(len(symbols_nobitex)))
              #for symbol in symbols_nobitex:
                #     print(symbol)
              #value=self.get_orderbook('all')
              value=self.get_orderbook(symbol)
              
              if(value):
                     #Asks.update({symbol:value['asks']})
                     #sleep(0.1)
                  #for sym in symbols_nobitex:
                     print(symbol)
                     #if(value[symbol]):
                            #all
                            #lastUpdate=value[symbol]['lastUpdate']
                            #lastTradePrice=value[symbol]['lastTradePrice']
                     lastUpdate=value['lastUpdate']
                     lastTradePrice=value['lastTradePrice']
                     bids=value['bids']
                     print("lastUpdate:{} ,lastTradePrice:{}".format(lastUpdate,lastTradePrice))
                     #all
                     #asks=value[symbol]['asks']
                     print("bids:\n price      bid")
                     for price,bid in bids:#key:price,val:ask
                            bids_list.append(bid)
                            if(float(bid)>config1 and float(bid)<config2):
                                   print(price,bid)
                                   PriceBid_list.append({"price":price,"bid":bid})
                     Bids.update({symbol:PriceBid_list,"lastUpdate":lastUpdate,'lastTradePrice':lastTradePrice})
                     print(len(PriceBid_list))
                     if(len(PriceBid_list)==0):
                            min_bid=min(bids_list)
                            max_bid=max(bids_list)
                            Bids.update({symbol:{"min_bid":min_bid,"max_bid":max_bid}})
              return Bids

               
#               DepthCache.get_bids()
       def BidAskRatio(self,ratio):#4
               BidsRatio=[]
               BidsRatiodic={}
               PriceAsks_list=[]
               PriceBids_list=[]
               value= self.get_orderbook('all')
               sleep(0.01)
               for symbol in symbols_nobitex:
                            print(symbol)
                            if(value[symbol]):
                                   lastUpdate=milliseconds_to_date(value[symbol]['lastUpdate'])
                                   lastTradePrice=value[symbol]['lastTradePrice']
                                   print("lastUpdate:{} ,lastTradePrice:{}".format(lastUpdate,lastTradePrice))
                                   asks=value[symbol]['asks']#[price,ask]
                                   bids=value[symbol]['bids']#[price,bid]
                                   print(asks)
                                   num_asks=len(asks)
                                   num_bids=len(bids)
                                   #if(num_asks > num_bids):
                                   print("num_asks:{}  num_bids:{}".format(num_asks,num_bids))
                                   print("symbol   pricea   ask    ratio  priceb  bid")
                                   #if( num_asks== num_asks):
                                   '''
                                   for i in range(len(asks)):
                                         ask=float(asks[i][1])
                                         bid=float(bids[i][1])
                                         PriceAsks_list.append(ask)
                                         PriceBids_list.append(bid)
                                         if(ask> ratio * bid):
                                                print(symbol,asks[i][0],ask,ratio,bids[i][0],bid)
                                                BidsRatio.append({'pricea':asks[i][0],'ask':ask,'ratio':ratio,'priceb':bids[i][0],'bid':bid})
                                   #else:
                                          #print(' num_asks no
                                   
                                   '''       
                                   for pricea,ask in asks:
                                          ask=float(ask)
                                          PriceAsks_list.append(ask)
                                          for priceb,bid in bids:
                                                  bid=float(bid)
                                                  if (bid not in  PriceBids_list):
                                                         PriceBids_list.append(bid)
                                                  if(ask > ratio * bid):
                                                         print(symbol,pricea,ask,ratio,priceb,bid)
                                                         BidsRatio.append({'pricea':pricea,'ask':ask,'ratio':ratio,'priceb':priceb,'bid':bid})
                                  
                            if(len(BidsRatio)==0):
                                 print("len is zero.")
                            if(len(PriceAsks_list)!=0):
                                 max_asks=max(PriceAsks_list)
                                 min_asks=min(PriceAsks_list)
                                 max_bids=max(PriceBids_list)
                                 min_bids=min(PriceBids_list)
                                 print('max_asks: {}  min_asks:{}  max_bids:{}  min_bids:{}'.format(max_asks,min_asks,min_bids,max_bids))
                                 BidsRatio.append({'max_asks':max_asks,'min_asks':min_asks,'max_bids':max_bids,'min_bids': min_bids,'lastUpdate':lastUpdate,'lastTradePrice':lastTradePrice})
                            BidsRatiodic[symbol]=BidsRatio
                            BidsRatio=[]
               
                                                   
               print(len(BidsRatiodic))                                    
               return BidsRatiodic              
  #             DepthCache.get_bids()
       def AskBidRatio(self,ratio):#5
             AsksRatio=[]
             PriceAsks_list=[]
             PriceBids_list=[]
             AsksRatiodic={}
             value= self.get_orderbook('all')
             for symbol in symbols_nobitex:
                     print(symbol)
                     if(value[symbol]):
                            lastUpdate=milliseconds_to_date(value[symbol]['lastUpdate'])
                            lastTradePrice=value[symbol]['lastTradePrice']
                            print("lastUpdate:{} ,lastTradePrice:{}".format(lastUpdate,lastTradePrice))
                            asks=value[symbol]['asks']
                            bids=value[symbol]['bids']
                            num_asks=len(asks)
                            num_bids=len(bids)
                            #if(num_asks > num_bids):
                            print("num_asks:{}  num_bids:{}".format(num_asks,num_bids))
                            print("symbol   pricea   ask    ratio  priceb  bid")
                            for pricea,ask in asks:
                                   ask=float(ask)
                                   PriceAsks_list.append(ask)
                                   for priceb,bid in bids:
                                          bid=float(bid)
                                          if (bid not in  PriceBids_list):
                                                PriceBids_list.append(bid)
                                          if(ask * ratio < bid):#diff
                                                   print(symbol,pricea,ask,ratio,priceb,bid)
                                                   AsksRatio.append({'pricea':pricea,'ask':ask,'ratio':ratio,'priceb':priceb,'bid':bid})
                     if(len(AsksRatio)==0):
                            print("len is zero.")
                     if(len(PriceAsks_list)!=0):
                                 max_asks=max(PriceAsks_list)
                                 min_asks=min(PriceAsks_list)
                                 max_bids=max(PriceBids_list)
                                 min_bids=min(PriceBids_list)
                                 print('max_asks: {}  min_asks:{}  max_bids:{}  min_bids:{}'.format(max_asks,min_asks,min_bids,max_bids))
                                 AsksRatio.append({'max_asks':max_asks,'min_asks':min_asks,'max_bids':max_bids,'min_bids': min_bids,'lastUpdate':lastUpdate,'lastTradePrice':lastTradePrice})
                     AsksRatiodic[symbol]=AsksRatio
                     AsksRatio=[]
             return AsksRatiodic
    #           DepthCache.get_asks()
       def Spread(self,spread):#6 #ask-bid >spread
            
             Spreaddic={}
             Spread=[]
             
             PriceAsks_list=[]
             PriceBids_list=[]
             
             value= self.get_orderbook('all')
             for symbol in symbols_nobitex:
                     print(symbol)
                     if(value[symbol]):
                            lastUpdate=milliseconds_to_date(value[symbol]['lastUpdate'])
                            lastTradePrice=value[symbol]['lastTradePrice']
                            print("lastUpdate:{} ,lastTradePrice:{}".format(lastUpdate,lastTradePrice))
                            asks=value[symbol]['asks']
                            bids=value[symbol]['bids']
                            num_asks=len(asks)
                            num_bids=len(bids)
                            #if(num_asks > num_bids):
                            print("num_asks:{}  num_bids:{}".format(num_asks,num_bids))
                            print("symbol   pricea   ask    ratio  priceb  bid")
                            for pricea,ask in asks:
                                   ask=float(ask)
                                   PriceAsks_list.append(ask)
                                   for priceb,bid in bids:
                                          bid=float(bid)
                                          if (bid not in  PriceBids_list):
                                                PriceBids_list.append(bid)
                                          Spread_val=ask - bid
                                          if(Spread_val> spread):#diff
                                                   print(symbol,pricea,ask,spread,priceb,bid)
                                                   Spread.append({'pricea':pricea,'ask':ask,'spread':spread,'priceb':priceb,'bid':bid})
                     if(len(Spread)==0):
                            print("len is zero.")
                     if(len(PriceAsks_list)!=0):
                                 max_asks=max(PriceAsks_list)
                                 min_asks=min(PriceAsks_list)
                                 max_bids=max(PriceBids_list)
                                 min_bids=min(PriceBids_list)
                                 print('max_asks: {}  min_asks:{}  max_bids:{}  min_bids:{}'.format(max_asks,min_asks,min_bids,max_bids))
                                 Spread.append({'max_asks':max_asks,'min_asks':min_asks,'max_bids':max_bids,'min_bids': min_bids,'spread_max':max_asks-min_bids,'lastUpdate':lastUpdate,'lastTradePrice':lastTradePrice})
                     Spreaddic[symbol]=Spread
                     Spread=[]
             return  Spreaddic
       def AverageDailyVolume(symbol):#7
                   #ticker24hour=client.get_ticker()
                   #klines=client.get_historical_klines(symbol,candle_type,"2 day ago UTC")
                   candle_type='D'
                   #today_klines='1669109317'
                   now_time=str(int(time()))
                   thirty_month_time=today_time-timedelta(days=30)
                   ohcl_nobitex=self.get_OHCL_N(symbol,candle_type,thirty_month_time,now_time)
                   ohcl=ohcl_nobitex['symbol'][-1]
                   print(ohcl)
                   if(ohcl['v'] >TodaysVolume):
                                 print("volume daily >TodaysVolume")
                   return  ohcl_nobitex
       def TodaysVolume(self,symbol,TodaysVolume):#8
                   #ticker24hour=client.get_ticker()
                   #klines=client.get_historical_klines(symbol,candle_type,"2 day ago UTC")
                   candle_type='60'
                   #today_klines='1669109317'
                   now_time=datetime.now()
                   yesterday_time=str(datetime_to_epoch(now_time-timedelta(days=10000)))
                   now_time_ms=str(datetime_to_epoch(now_time))
                   print(now_time_ms)
                   print(yesterday_time)
                   ohcl_nobitex=self.get_OHCL_N(symbol,candle_type,yesterday_time,now_time_ms)
                   print("hi")
                   if( ohcl_nobitex):
                              
                          #if(ohcl_nobitex['status']!='failed'):
                                 print("hi")
                                 ohcl=ohcl_nobitex[symbol][-1]
                                 print(ohcl)
                                 if(ohcl['volume'] >TodaysVolume):
                                               print("volume daily >TodaysVolume")
                                               return  ohcl
                   else:
                          return ohcl_nobitex
       def OneDayVolumeRatio():#9
                   #ticker24hour=client.get_ticker()
                   #klines=client.get_historical_klines(symbol,candle_type,"2 day ago UTC")
                   candle_type='D'
                   #today_klines='1669109317'
                   now_time=str(int(time()))
                   yesterday_time=today_klines-timedelta(hours=24)
                   ohcl_nobitex=self.get_OHCL_N(symbol,candle_type,yesterday_time,now_time)
                   ohcl_today=ohcl_nobitex['symbol'][-1]
                   ohcl_yesterday=ohcl_nobitex['symbol'][-2]
                   
       def RelativeVolumeRatio():#10
                    #ticker24hour=client.get_ticker()
#                    klines=client.get_historical_klines(symbol,candle_type,"2 day ago UTC")
                    ohcl_nobitex=get_OHCL_N(symbol,candle_type,frm,to)
       def YesterdayVolumeRatio():#11
                   ticker24hour=client.get_ticker()
                   klines=client.get_historical_klines(symbol,candle_type,"2 day ago UTC")
                   ohcl_nobitex=get_OHCL_N(symbol,candle_type,frm,to)
       def VolatilityMinutes(tm):#60m,15m  12
              pass
       #def Volatility60Minutes():
       #def Volatility15Minutes():
       def MinuteVolumeRatio(tm):#1m5m,15m,60m  13
               pass
       #def 1MinuteVolumeRatio():
       #def 5MinuteVolumeRatio():
       #def 1minuteVolumeRatio(): 
       #def 60MinuteVolumeRatio():
       def AverageTrueRange():#14
               pass
       def TodaysRange():#15
               pass
                       
       def MinuteRange(tm):#1m,5m,15m,60m  16
               pass
       #def 1 minute range():
       #def 5 minute range():
       #def 15 minute range():
       #def 60 minute range():
       def minutePercentChange():#1m,5m,15m,60m  17
              pass
       #def 1 minute % change():
       #def 5 minute % change():
       #def 15 minute % change():
       #def 60 minute % change():
       
       def DailyPositiveCandle():#18
               pass
       def MinutesPositiveCandle(tm):#1m,5m,15m,60 19
               pass
       #def 1MinutesPositiveCandle():
       #def 5MinutesPositiveCandle():
       #def 15MinutesPositiveCandle():
       #def 60MinutesPositiveCandle():
                                       
       def DailyNegativeCandle():#20
               pass
       def MinutesNegativeCandle(tm):#1m,5m,15m,60m   21
               pass
       #def 1MinutesegativeCandle():
       #def  5MinutesegativeCandle():
       #def  15MinutesegativeCandle():
       #def  60MinutesegativeCandle():
                       
       def  PercentDownYesterday():#22
               pass
       def PercentUPYesterday():#23
               pass
                       
       def AverageNumberofPrintsTrades():#24
               pass
       def MarketCap():#25
               pass
                       
       def NewHigh():#26
               pass
       def NewLow():#27
               pass
       def CrossedDailyHighs():#28
               pass
       def CrossedDailyLows():#29
               pass
       def NewHighWithMinimumChange():#30
               pass
       def NewLowWithMinimumChange():#31
               pass
       def PercentUpForTheDay():#32
               pass
       def PercentDownForTheDay():#33
               pass 
                       
       def SignificantAskSize():#34
               pass
       def SignificantBidSize():#35
               pass

       def BigSizeTrade():#36
               pass
                       
       def ConsolidationRangeMinutes(tm):#60m,15m,5m  37
               pass
       #def ConsolidationRange60Minutes():
       #def ConsolidationRange15Minutes():
       #def ConsolidationRange5Minutes():
                       
       def RelativeVolumeUp():#38
                       pass
       def SuddenVolumeSpikeRatio():#39
                       pass
                       
                       
       def MinuteVolumeSpikeRatio(tm):#5m,15m,60m   40
               pass
       #def 5MinuteVolumeSpikeRatio():
       #def 15MinuteVolumeSpikeRatio():
       #def 60MinuteVolumeSpikeRatio():


       def UnusualNumberofTradesm(tm):#1m,5m,15m,60m   41
               pass
       #def UnusualNumberofTrades1m():
       #def UnusualNumberofTrades5m():
       #def UnusualNumberofTrades15m():
       #def UnusualNumberofTrades60m():


       def SpikeUpPercent():#42
               pass
       def SpikeDownPercent():#43
               pass

