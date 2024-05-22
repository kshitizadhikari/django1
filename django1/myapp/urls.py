from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('create-article/', views.create_article, name='create-article'),
    path('article/<int:article_id>/', views.get_article, name='get-article'),
]