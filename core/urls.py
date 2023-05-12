from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('home', views.home, name='home'),
    path('book_list/', views.BookList.as_view(), name='book_list'),
    path('author_detail/<int:pk>', views.AuthorDetail.as_view(), name='author'),
    path('book_create/', views.BookCreate.as_view(), name='book_create'),
    path('book_update/<int:pk>', views.BookUpdate.as_view(), name='book_update'),
    path('book_delete/<int:pk>', views.BookDelete.as_view(), name='book_delete')
    #path('book_list/', views.get_book_list, name='book_list'),
    #path('author_detail/<int:pk>', views.get_author, name='author'),
]
