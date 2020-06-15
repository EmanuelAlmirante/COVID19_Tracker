from django.conf.urls import url
from covid_tracker_backend import views

urlpatterns = [
    url(r'^api/covidtracker$', views.data_list),
    url(r'^api/covidtracker/(?P<pk>[0-9]+)$', views.country_details),
    #url(r'^api/tutorials/(\w[a-zA-Z]+)$', views.country_data)
]
