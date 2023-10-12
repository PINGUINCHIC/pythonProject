from django.urls import path
from .views import PostList, PostDetail, News, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'newapp'
urlpatterns = [
    path('', PostList.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name='new_detail'),
    path('search/', News.as_view(), name='search'),
    path('new/create/', PostCreateView.as_view(), name='new_create'),
    path('new/update/<int:pk>/', PostUpdateView.as_view(), name='new_update'),
    path('new/delete/<int:pk>/', PostDeleteView.as_view(), name='new_delete'),
]