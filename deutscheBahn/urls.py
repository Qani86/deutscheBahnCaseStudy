from django.urls import path

from deutscheBahn.views import deutscheBahn

urlpatterns = [
    path('', deutscheBahn),
]