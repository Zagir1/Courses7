from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('book_list/', views.get_book_list, name='book_list'),
    #path('book_list/', views.ListView.as_view(), name='book_list'),
    path('author_detail/<int:pk>', views.AuthorDetail.as_view(), name='author'),
    #path('author_detail/<int:pk>', views.get_author, name='author'),
]
