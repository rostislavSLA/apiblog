from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author_email = serializers.EmailField(source='author.email', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'author', 'author_email', 'access']

        extra_kwargs = {
            'author': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if instance.author != self.context['request'].user:
            raise serializers.ValidationError("You don't have permission to edit this article")
        return super().update(instance, validated_data)
