from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^info/$', FileInfoView.as_view(), name='GetFileInfo'),
    url(r'^info/$', FileInfoView.as_view(), name='PostFileInfo'),
    url(r'^process/$', RunProcess.as_view(),name='RunProcess'),
    url(r'^time_series/$', GetTimeSeries.as_view(), name='GetTimeSeries'),
    url(r'^psd/$', GetPSD.as_view(), name='GetPSD'),
    url(r'^time_frequency/$', GetTimeFrequency.as_view(), name='GetTimeFrequency'),
    url(r'^events/$', GetEvents.as_view(), name='GetEvents'),
    url(r'^methods/filters/notch/$', NotchFilterView.as_view(),name='NotchFilter'),
    url(r'^methods/filters/custom/$', CustomFilterView.as_view(),name='CustomFilter'),
    url(r'^methods/peaks/$', GetPeaks.as_view(),name='GetPeaks'),
]
