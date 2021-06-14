from rest_framework import serializers
from blog.models import *


class PostSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'category', 'title')


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects, slug_field='title')
    title = serializers.CharField(required=True)
    descriptions = serializers.CharField(required=False)
    image = serializers.ImageField(required=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    created_at = serializers.DateField(required=True)

    class Meta:
        model = Post
        fields = ('id', 'category', 'slug', 'title', 'descriptions', 'image', 'created_at', 'price', 'favourite')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', )


# class CommentSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.username')
#
#     class Meta:
#         model = Comment
#         fields = ('user', 'post', 'email', 'body', )