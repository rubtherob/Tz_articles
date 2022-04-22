
from rest_framework import serializers

from article.models import Artcle


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artcle
        fields = '__all__'








