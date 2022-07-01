from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('portfolio/', views.PostList.as_view(), name='portfolio'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='portfolio_details'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
