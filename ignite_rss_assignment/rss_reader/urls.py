from django.conf.urls import url
from django.contrib import admin
from views import feed_view

urlpatterns = [
    url(r'^feed$',feed_view),

]
