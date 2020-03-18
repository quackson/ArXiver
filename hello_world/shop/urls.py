from django.urls import path

import shop.views

urlpatterns = [
    path('hello', shop.views.hello)
]