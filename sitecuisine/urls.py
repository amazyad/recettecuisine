from django.conf.urls import patterns, url
from sitecuisine.views import index

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
)