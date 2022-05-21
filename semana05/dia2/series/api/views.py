from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Series
from .serializers import SeriesSerializer

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class SeriesView(APIView):
    
    def get(self,request):
        dataSeries = Series.objects.all()
        serSeries = SeriesSerializer(dataSeries, many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSerie = SeriesSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
class SeriesDetailView(APIView):
    
    def get(self,request,serie_id):
        dataSerie = Series.objects.get(pk=serie_id)
        serSerie = SeriesSerializer(dataSerie)
        return Response(serSerie.data)
    
    def put(self,request,serie_id):
        dataSerie = Series.objects.get(pk=serie_id)
        serSerie = SeriesSerializer(dataSerie, data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
    def delete(self,request,serie_id):
        dataSerie = Series.objects.get(pk=serie_id)
        serSerie = SeriesSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)
    
    