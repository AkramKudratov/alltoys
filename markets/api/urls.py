from django.urls import path

from markets import views

app_name = 'markets-api'
urlpatterns = [
    path('', views.markets, name='markets'),
]
