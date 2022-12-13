from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import TbNews , TbCount, TbRecommend
from .serializers import NewsSerializer
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from django.http import HttpResponse
# Create your views here.


# 뉴스 하나 조회
@api_view(['GET'])
def detail(request, newsid):
    news = get_object_or_404(TbNews, pk=newsid)
    serializer = NewsSerializer(news)
    return Response(data = serializer.data, status = status.HTTP_200_OK)
    # return render(request, 'detail.html', {''})

# 최신 뉴스 조회 -> main 페이지
@api_view(['GET'])
def news_list(requests):
    # models.py의 TbNews 클래스의 모든 객체를 news에 담음
    news_many = TbNews.objects.all().order_by('-writedat')[:20] # 최신 순 정렬(20개)
    serializer = NewsSerializer(news_many, many=True)
    return Response(data = serializer.data, status = status.HTTP_200_OK)


# 코멘트 수 많은 뉴스대로 조회
# comment의 개수로 인기 있는 뉴스 보여주기
@api_view(['GET'])
def popular_news(requests):
    populars = TbCount.objects.all().order_by('-count')[:20]
    # serializer = NewsSerializer(pnews_many, many=True)
    serializer = NewsSerializer([p.newsid for p in populars], many=True)

    return Response(data = serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
def recommend_news(requests, newsid):
    reco = get_object_or_404(TbRecommend, pk=newsid)
    recom_list = reco.recommendation.replace('[', '').replace(']', '').split(',')
    news_list = TbNews.objects.filter(pk__in=recom_list)
    serializer = NewsSerializer(news_list, many=True)

    return Response(data = serializer.data, status = status.HTTP_200_OK)