from django.urls import path
from . import views


app_name = 'pages'
urlpatterns = [
    path('dinner/<str:menu>/<int:population>/', views.dinner, name='dinner'),
]
