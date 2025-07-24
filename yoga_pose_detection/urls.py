from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('yoga_train_pred.urls')),
    path('train_prediction/', include('yoga_train_pred.urls')),  # optional if you want both
]
