from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    path('index/', views.index, name = 'index'), # メインページ
]