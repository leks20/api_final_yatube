from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post, Comment, Follow, Group

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate_following(self, value):
        user = self.context['request'].user
        if Follow.objects.filter(user=user, following__username=value).exists():
            raise serializers.ValidationError("Вы уже подписаны на данного автора")
        return value


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title')
        model = Group
