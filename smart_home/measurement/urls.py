from django.urls import path
from . import views

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('<int:pk>/', views.RetrieveUpdateAPIView.as_view()),
    path('', views.ListSensors.as_view()),
    path('create/', views.CreateAPIView.as_view()),
    path('update/<int:pk>/', views.RetrieveUpdateAPIView.as_view()),
    path('add_measurement/', views.ListCreateAPIView.as_view()),
]
