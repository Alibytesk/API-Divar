from django.urls import path
from .views import *

app_name = 'ads'
urlpatterns = [
    path('list', AdListView.as_view(), name='ads'),
    path('add', AdCreateView.as_view(), name='add')
]