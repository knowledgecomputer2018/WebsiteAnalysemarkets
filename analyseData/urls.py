from django.urls import path
from analyseData import views


urlpatterns=[
       
       path('',views.AnalyseData,name='AnalyseData'),
#       path('trades/',views.get_Trades,name='get_Trades'),
  #     path('markets/',views.get_all_markets_global,name='get_markets'),
    #   path('ohcl/',views.get_OHCL,name='get_ohcl'),
      # path('orderbook/',views.get_orderbook,name='get_orderbook'),
      # path('depthorders/',views.get_depthorders,name='get_depthorders'),
      # path('token/',views.get_token,name='get_token'),

       #path('klines/',views.get_klines,name='get_klines'),
       
              
       path("projects/",views.project_index,name="project_index"),
       path("payment_crypto/",views.payment_crypto,name="payment_crypto"),
       path("projects/<int:pk>/",views.project_detail,name="project_detail"),

       path("algory/",views.algory_index,name="algory_index"),

       path("https://web.telegram.org/z/#-542503782",views.telegram_index,name="telegram_index"),
       

       ]
