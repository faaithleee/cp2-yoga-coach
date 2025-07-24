from django.urls import path
from . import views

urlpatterns = [
    path('', views.training_view, name='training'),
    path('train/', views.training_view, name='train'),         # ✅ trailing slash
    path('prediction/', views.prediction_view, name='predict'), # ✅ trailing slash
    path('reference/', views.reference_view, name='reference'),
]
