from django.urls import path
from .views import SnacksListView,SnackDetailView
urlpatterns = [
    path('',SnacksListView.as_view(), name = 'snack_list'),
    path('<int:pk>',SnackDetailView.as_view(), name = 'snack_detail'),
]