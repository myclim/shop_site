from django.urls import path
from main.views import IndexView, ContactView


app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact')
]
