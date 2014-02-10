from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns('',
        url(r'^$', views.mainIndex, name='mainIndex'),
        url(r'^send', views.send, name='send'),
        url(r'^texts', views.texts, name='texts'),
        url(r'^call', views.call, name='call'),
        url(r'^data/enterNearest', views.findNear, name='findNear'),
        url(r'^data/addNewWorker', views.enterNew, name='enterNew'),
        url(r'^data', views.data, name='data'),
)
   
