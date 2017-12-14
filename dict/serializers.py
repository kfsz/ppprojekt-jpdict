from rest_framework import routers, serializers, viewsets
from .models import Word, WordTL

#for api

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('word', 'reading', 'common')

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.order_by('-word')[:2000]   #all()
    serializer_class = WordSerializer
    
class MoreWordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.order_by('-word')[:5000]   #all()
    serializer_class = WordSerializer