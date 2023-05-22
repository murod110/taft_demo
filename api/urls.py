from django.urls import path
from .views import BotUserAPIView, FeedbackAPIView, ProductAPIView, QualityAPIView, PaletAPIView, CharakterAPIView, DesignAPIView 


urlpatterns = [
    path('bot-users',BotUserAPIView.as_view(),name='bot-users'),
    path('bot-feedback',FeedbackAPIView.as_view(),name='bot-feedback'),
    path('product-api',ProductAPIView.as_view(),name="product-api"),
    path('quality',QualityAPIView.as_view(),name="quality-api"),
    path('palet', PaletAPIView.as_view(),name="palet"),
    path('charakter',CharakterAPIView.as_view(),name="charakter"),
    path('design',DesignAPIView.as_view(),name="design")
]