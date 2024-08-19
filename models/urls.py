from tkinter.font import names

from django.urls import path
from .views import contact_page, success

urlpatterns = [
    path('', contact_page),
    path('success', success, name="success")
]