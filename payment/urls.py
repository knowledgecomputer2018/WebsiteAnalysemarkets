from django.urls import path
from payment import views


urlpatterns=[
       path('',views.home,name="home"),
       path('economic',views.economic,name="economic"),
       #tranfer argument to view function 
       path('create/<pk>',views.create_payment,name="create_payment"),
       #tranfer pk views to url path(reverse)
       path('payment/invoice/<pk>',views.track_invoice,name="track_payment"),
       path('payments/receive/', views.receive_payment, name='receive_payment'),
       ]

