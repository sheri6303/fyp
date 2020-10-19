from django.urls import path
from . import views

urlpatterns=[
    path('', views.hello, name='hello'),

    path('printmyname',views.printMyName,name='printmyname'),

    path('printdynamichtml', views.printDynamic, name='printdynamic')

]
