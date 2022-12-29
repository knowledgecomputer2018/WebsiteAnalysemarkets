from django import forms

    
Scanner_Markets_Choices=[
('GetAllMarketsGlobalN','GetAllMarketsGlobalNobitex'),
('GetTradesN','GetTradesNobitex'),
('GetOrderbookN','GetOrderbookNobitex'),
('PriceRange','Price range'),
('AskSize','Ask size'),
('BidSize','Bid size'),
('BidAskRatio','Bid Ask ratio'),
('AskBidRatio','Ask Bid ratio'),
('Spread','Spread'),
('AverageDailyVolume','Average daily volume'),
('TodaysVolume','Todays volume'),
('1DayVolumeRatio','1 day volume ratio'),
('RelativeVolumeRatio','Relative volume ratio'),		
('YesterdayVolumeRatio','Yesterday volume ratio'),
('Volatility60Minutes','Volatility 60 minutes'),
('Volatility15Minutes','Volatility 15 minutes'),
('1MinuteVolumeRatio','1 minute volume ratio'),
('5MinuteVolumeRatio','5 minute volume ratio'),
('1minuteVolumeRatio','15 minute volume ratio'), 
('60MinuteVolumeRatio','60 minute volume ratio'),
		
		
		 
		
('AverageTrueRange','Average True Range'),
		
		
		 
		
('TodaysRange','Today`s range'),
		
		
		 
		
('1 minute range','1 minute range'),
		
		
		 
		
('5 minute range','5 minute range'),
		
		
		 
		
('15 minute range','15 minute range'),
		
		
		 
		
('60 minute range','60 minute range'),
('1 minute range','1 % minute range'),
		
		
		 
		
('5 minute range','5 % minute range'),
		
		
		 
		
('15 minute range','15 % minute range'),
		
		
		 
		
('60 minute range','60 % minute range'),
		
		
		 
		
('DailyPositiveCandle','Daily positive candle'),
		
('1MinutesPositiveCandle','1 minutes positive candle'),
		
		
		 
		
('5MinutesPositiveCandle','5 minutes positive candle'),
		
		
		 
		
('15MinutesPositiveCandle','15 minutes positive candle'),
		
		
		 
		
('60MinutesPositiveCandle','60 minutes positive candle'),
		
		
		
		 
		
('1MinutesPositiveCandle','1 minutes positive candle'),
		
		
		 
		
('5MinutesPositiveCandle','5 minutes positive candle'),
		
		
		 
		
('15MinutesPositiveCandle','15 minutes positive candle'),
		
		
		 
		
('60MinutesPositiveCandle','60 minutes positive candle'),
		
		
		
		 
		
('DailyNegativeCandle','Daily negative candle'),
		
		
		 
		
('1MinutesNegativeCandle','1 minutes negative  candle'),
		
		
		 
		
('5MinutesegativeCandle','5 minutes negative  candle'),
		
		
		 
		
('15MinutesegativeCandle','15 minutes negative  candle'),
		
		
		 
		
('60MinutesegativeCandle','60 minutes negative  candle'),
		
		
		
		 
		
('%DownYesterday','% Down Yesterday'),
('%UPYesterday','% UP Yesterday'),
		
		
		 
		
('AverageNumberofPrints/Trades','Average number of prints / trades'),
		
		
		 
		
('MarketCap','Market Cap'),
		
		
		 
		
('NewHigh','New high'),
('NewLow','New low'),
		
		
		 
		
('CrossedDailyHighs','Crossed daily highs'),
('CrossedDailyLows','Crossed daily lows'),
		
		
		 
		
('NewHighWithMinimumChange','New high with minimum change'),
('NewLowWithMinimumChange','New low with minimum change'),
		
		
		 
		
('% UpForTheDay','% up for the day'),
('% DownForTheDay','% down for the day'),
		
		
		 
		
('SignificantAskSize','Significant ask size'),
('SignificantBidSize','Significant bid size'),

('BigSizeTrade','Big size trade'),
		
		
		 
		
('ConsolidationRange60Minutes','Consolidation range 60 minutes'),
('ConsolidationRange15Minutes','Consolidation range 15 minutes'),
('ConsolidationRange5Minutes','Consolidation range 5 minutes'),
		
		
		 
		
('RelativeVolumeUp','Relative volume up'),
		
		
		 
		
('SuddenVolumeSpikeRatio','Sudden volume spike ratio'),
		
		
		 
		
('5MinuteVolumeSpikeRatio','5 Minute Volume Spike ratio'),
('15MinuteVolumeSpikeRatio','15 Minute Volume Spike ratio'),
('60MinuteVolumeSpikeRatio','60 Minute Volume Spike ratio'),


		
		 
		
('UnusualNumberofTrades1m','Unusual number of trades 1m'),
('UnusualNumberofTrades5m','Unusual number of trades 5m'),
('UnusualNumberofTrades15m','Unusual number of trades 15m'),
('UnusualNumberofTrades60m','Unusual number of trades 60m'),


('SpikeUp %','Spike up %'),
('SpikeDown %','Spike down %'),

    ]
class filterForm(forms.Form):
    dropDownFilter = forms.CharField (
        label="dropDownFilter:",
        max_length=66,
        widget=forms.Select(choices=Scanner_Markets_Choices,
        attrs = {
            'onchange' : " \
            if(document.getElementById('id_dropDownFilter'))\
            {\
                d=document.getElementById('id_dropDownFilter').value;\
                console.log(d);\
            }\
            if(d)\
            {\
                desc = document.getElementById(d);\
                if(desc)\
                    {\
                        console.log(desc.style.display );\
                        console.log(d);\
                        if (d=='PriceRange' & desc.style.display === 'none') {\
                             desc.style.display = 'block';\
                        }\
                        else if (d=='AskSize' & desc.style.display === 'none') {\
                                desc.style.display = 'block';\
                                config2=document.getElementById('id_config');\
                                config1.placeholder='min';\
                                config2.placeholder='max';\
                        }\
                        else if (d=='BidSize' & desc.style.display === 'none') {\
                                desc.style.display = 'block';\
                                config1=document.getElementById('id_config1');\
                                config2=document.getElementById('id_config');\
                                config1.placeholder='min';\
                                config2.placeholder='max';\
                            }\
                         else if (d=='AskBidRatio' & desc.style.display === 'none') {\
                                 desc.style.display = 'block';\
                                 config1=document.getElementById('id_config1');\
                                 config1.placeholder='ratio';\
                                    }\
                         else if (d=='BidAskRatio' & desc.style.display === 'none') {\
                                  desc.style.display = 'block';\
                                  config1=document.getElementById('id_config1');\
                                  config1.placeholder='ratio';\
                            }\
                          else if (d=='Spread' & desc.style.display === 'none') {\
                                    desc.style.display = 'block';\
                                    config1=document.getElementById('id_config1');\
                                    config1.placeholder='spread';\
                            }\
                            else if (d=='TodaysVolume' & desc.style.display === 'none') {\
                                    desc.style.display = 'block';\
                                    config1=document.getElementById('id_config1');\
                                    config1.placeholder='volume';\
                            }\
                         else\
                            {\
                                desc.style.display = 'none';\
                            }\
                    }\
                else\
                            {desc.style.display = 'none';}\
            }"
            }),
    )
    symbol= forms.CharField(
            max_length=100,
            widget=forms.TextInput(attrs={ "class": "form-control", "placeholder": "symbols" }
                )
            )
    config1 = forms.CharField(
            max_length=10,
            widget=forms.TextInput(attrs={ "class": "form-control", "placeholder": "Config1" }
                )
            )
    config2 = forms.CharField(
            max_length=10,
            widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Config2"}
                )
            )
'''
config2=document.getElementById('id_config2');\
                                config2.style.opacity=100;\
                                config2.placeholder='max';\
                                config1=document.getElementById('id_config1');\
                                config1.style.opacity=100;\
                                 config1.placeholder='min';\
'''


