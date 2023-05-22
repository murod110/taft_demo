from .models import BotUser, Feedback, Palet, Charakter
from app.models import Product, Quality, Design
from .serializers import BotUserSerializer, FeedbackSerializer, ProductAPI,QualityAPI, PaletSerializer, DesignSerializer, CharakterSerializer
from rest_framework.generics import ListCreateAPIView

class BotUserAPIView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer

class FeedbackAPIView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAPI


class QualityAPIView(ListCreateAPIView):
    queryset = Quality.objects.all()
    serializer_class = QualityAPI

class PaletAPIView(ListCreateAPIView):
    queryset = Palet.objects.all()
    serializer_class = PaletSerializer

class CharakterAPIView(ListCreateAPIView):
    queryset = Charakter.objects.all()
    serializer_class = CharakterSerializer

class DesignAPIView(ListCreateAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer