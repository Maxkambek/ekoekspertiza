from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News, Calculator, Spirituality, Branch, Management, Director, Partner, Document, CenterTarkibi
from .serializers import NewsSerializer, SpiritualitySerializer, BranchSerializer, ManagementSerializer, \
    DirectorSerializer, PartnerSerializer, DocumentSerializer, CenterTarkibiSerializer


class CenterTarkibiListAPIView(generics.ListAPIView):
    queryset = CenterTarkibi.objects.all()
    serializer_class = CenterTarkibiSerializer


class DocumentListAPIView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class PartnerListAPIView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class SpiritualityListAPIView(generics.ListAPIView):
    queryset = Spirituality.objects.all()
    serializer_class = SpiritualitySerializer


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'


class CalculatorAPIView(APIView):

    def get(self, request):
        q = self.request.GET.get('id')
        qs = Calculator.objects.order_by('-id').first()
        price = 0
        try:
            if q and int(q) == 1:
                price = int(qs.price) * 25
            if q and int(q) == 2:
                price = int(qs.price) * 15
            if q and int(q) == 3:
                price = int(qs.price) * 7.5
            if q and int(q) == 4:
                price = int(qs.price) // 2

            return Response({"data": str(price)}, status=200)
        except:
            return Response({"message": 'Enter valid data'}, status=404)


class BranchSerializerListAPIView(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class ManagementListAPIView(generics.ListAPIView):
    serializer_class = ManagementSerializer

    def get_queryset(self):
        q = self.request.GET.get('id')
        qs = Management.objects.all()
        if q:
            qs = qs.filter(branch_id=q)
        return qs


class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
