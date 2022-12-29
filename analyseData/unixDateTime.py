
from datetime  import  datetime
from pytz import timezone
import pytz
import dateparser
#import sample_config


'''
type datetime:
    1-datetime
    2-epoch unix datetime
    3-milliseconds datetime
'''
def datetime_to_epoch(d1):

    # create 1,1,1970 in same timezone as d1
    d2 = datetime(1970, 1, 1, tzinfo=d1.tzinfo)
    time_delta = d1 - d2
    ts = int(time_delta.total_seconds())
    return ts


def epoch_to_datetime(ts, tz_name="UTC"):
    format_datetime="%m/%d/%Y %H:%M:%S%p"
    #type datetime(d1) >change type str(x) >change format and type datetime
    x_timezone = timezone(tz_name)
    d1 = datetime.fromtimestamp(ts, x_timezone)#type datetime
    #strptime = "string parse time"
    x = d1.strftime("%m/%d/%Y %H:%M:%S%p")#type str
    #strftime = "string format time"
    x1=datetime.strptime(x,format_datetime)#type datetime,change format
    return x1
def milliseconds_to_date(milliseconds):#output string,where is datetime location?
        format_datetime='%Y-%m-%d %H:%M:%S.%f'
        #format_datetime='%m/%d/%Y %I:%M:%S%p'
        s = milliseconds/ 1000.0
        dte_str = datetime.fromtimestamp(s).strftime(format_datetime) #type string
        #return dte.split() #return date and time
        dte_datetime=datetime.strptime(dte_str, format_datetime) #change format(type datetime)
        return dte_datetime
def date_to_milliseconds(date_str):
    """Convert UTC date to milliseconds

    If using offset strings add "UTC" to date string e.g. "now UTC", "11 hours ago UTC"

    See dateparse docs for formats http://dateparser.readthedocs.io/en/latest/

    :param date_str: date in readable format, i.e. "January 01, 2018", "11 hours ago UTC", "now UTC"
    :type date_str: str
    """
    # get epoch value in UTC
    epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)
    # parse our date string
    d = dateparser.parse(date_str)
    # if the date is not timezone aware apply UTC timezone
    if d.tzinfo is None or d.tzinfo.utcoffset(d) is None:
        d = d.replace(tzinfo=pytz.utc)

    # return the difference in time
    return int((d - epoch).total_seconds() * 1000.0)


def interval_to_milliseconds(interval):
    """Convert a Binance interval string to milliseconds

    :param interval: Binance interval string 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
    :type interval: str

    :return:
         None if unit not one of m, h, d or w
         None if string not in correct format
         int value of interval in milliseconds
    """
    ms = None
    seconds_per_unit = {
        "m": 60,
        "h": 60 * 60,
        "d": 24 * 60 * 60,
        "w": 7 * 24 * 60 * 60
    }

    unit = interval[-1]
    if unit in seconds_per_unit:
        try:
            ms = int(interval[:-1]) * seconds_per_unit[unit] * 1000
        except ValueError:
            pass
    return ms

def change_timezone(dte,zone):#dte type is datetime
    #return dte.replace(tzinfo=timezone(zone))
    #format_datetime='%m/%d/%Y %I:%M:%S%p'
    time_zone = timezone(zone)
    with_timezone = dte.astimezone(time_zone)
    #dte_datetime=datetime.strptime(with_timezone, format_datetime) #change format(type datetime)
    #with_timezone = time_zone.localize(dte)
    return with_timezone


def TypesDateTimefun(StartTrade,EndTrade,now1,event_time_candle,candleTimeStartBar,candleTimeEndBar,now2,server_binance,):
    #----------------------Part of datetime now  ------------

    format_datetime='%Y-%m-%d %H:%M:%S.%f'
    
    #type Unix Epoch Time now (time.time())
    time_now1=epoch_to_datetime(now1)
    
    time_now2=epoch_to_datetime(now2)
    #time_now2_str=milliseconds_to_date(now2)
    #time_now2= datetime.strptime(time_now2_str, format_datetime)
    
    #serverlocalstartTrade=epoch_to_datetime(StartTrade)
    #serverlocalendTrade=epoch_to_datetime(EndTrade)
    
    
    
    server_binance=milliseconds_to_date(server_binance)
    #server_binance= datetime.strptime(server_binance_str, format_datetime)
    
    #candle_Time_Start_bar=milliseconds_to_date(candleTimeStartBar)
    #candle_Time_Start_bar= datetime.strptime(candle_Time_Start_bar_str, format_datetime)

    #candle_Time_End_bar=milliseconds_to_date(candleTimeEndBar)
    #candle_Time_End_bar= datetime.strptime(candle_Time_End_bar_str, format_datetime)
    
    iran_zone=sample_config.Settings_WhenTrade["WhenTrade"]["Zone"]

    #event_time_candle_datetime=milliseconds_to_date(event_time_candle) #event_time_candle :millisecond
    #event_time_candle_datetime=datetime.strptime(event_time_candle_str,format_datetime)
    
    
    TypesDateTime={
        "TypesDateTime":{ 
              #all values is string else not output in telegram robot .
                "ServerlocalGermany":{
                   
                    "DatetimeNow":{
                        "Centos":{
                                "DatetimeDotnow":str(time_now1),#error:do not global varible
                                "timeDottime":str(time_now2)
                            }
                        },
                    "ServerTelegram":"rightmessage",
                    "serverBinance":str(server_binance),
                    "Candle":{
                    
                    	
                        "StartTimeBar":str(candleTimeStartBar),# start time of this bar
                        "EndTimeBar":str(candleTimeEndBar),# end time of this bar
                        "CandleEventTime":str(event_time_candle)#event time
                        }
                   
                    
                },
                "MylocalIran":{
                    #"StarttimeTrade":str(change_timezone(serverlocalstartTrade+timedelta(hours=2,minutes=30),'Asia/Tehran')),
                   
                    "Datetimenow":{
                        "windows8.1":{
                              "DatetimeDotnow":str(change_timezone(time_now1,iran_zone)),
                              "timeDottime":str(change_timezone(time_now2,iran_zone))
                                
                                }
                            },
                    "ServerTelegram":"rightmessage",
                    "serverBinance":str(change_timezone(server_binance,iran_zone)),
                    "Candle":{
                        "StartTimeBar":str(change_timezone(candleTimeStartBar,iran_zone)),
                        "EndTimeBar":str(change_timezone(candleTimeEndBar,iran_zone)),
                        "CandleEventTime":str(change_timezone(event_time_candle,iran_zone))
                        }
                    
                }
            }
        }
    
    return TypesDateTime
'''
               
'''

#print(milliseconds_to_date(1638793882346))
'''
import pytz
d_naive =datetime.now()
tz_ber = pytz.timezone('Europe/Berlin')
tz_Teh = pytz.timezone('Asia/Tehran')
berlin_now = datetime.now(tz)
print(d_naive)
prit(berlin_now)
'''
#print(milliseconds_to_date(1633244700088))
