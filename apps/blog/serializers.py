from rest_framework import serializers

from blog.models import Article,User,Tag,Category

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar','username')

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ArticleSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    tag = TagSerializers(many=True)
    category = CategorySerializers()
    class Meta:
        model = Article
        fields = "__all__"
