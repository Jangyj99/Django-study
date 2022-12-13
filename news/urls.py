app_name = 'news'

from django.urls import path
from .import views

urlpatterns = [
    path('',views.news_list), # 뉴스 정렬
    path('<int:newsid>/', views.detail), # 하나의 뉴스 정보
    path('popular/', views.popular_news), # comment 개수 많은 순서
    path('<int:newsid>/con_recom', views.recommend_news), 
]

