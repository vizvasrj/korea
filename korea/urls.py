from django.contrib import admin
from django.urls import path
from korean.views import KonlpyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', KonlpyView.as_view(), name='korean'),
]
