from django.urls import path
from blog import views


urlpatterns=[
       
       path("",views.blog_index,name="blog_index"),
       #problem is priority that sovled by change
       #
       path("<int:pk>/",views.blog_detail,name="blog_detail"),
       path("<category>/",views.blog_category,name="blog_category"),
       
       path("https://knowledgecomputer2018.github.io/index2.html/",views.binance_index,name="binance_index"),
       ]
