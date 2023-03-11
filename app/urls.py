from django.urls import path
from .views import get_all_accounts, send_money
urlpatterns = [
    path('', get_all_accounts, name='get_all_accounts'),
    path('send_money', send_money,name='send_money')
    # path('unconnect/<int:pk>',unconnect,name="unconnect")
]
