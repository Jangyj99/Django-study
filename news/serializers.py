from rest_framework import serializers
from .models import TbNews, TbCount

# class CommentCountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TbCount
#         fields = ('id', 'count')

# db를 json으로 변환시켜줌
class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNews
        fields = ('id','maincategory', 'subcategory','title','content', 'writedat')
        


# class PopularSerializer(serializers.ModelSerializer): 
#     news = NewsSerializer(
#         read_only=True,
#     )

    # class Meta:
    #     model = TbCount
    #     fields = ()