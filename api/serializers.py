from .models import BotUser, Feedback, Palet, Charakter
from app.models import Product, Quality, Design
from rest_framework.serializers import ModelSerializer



class BotUserSerializer(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ("name","username","user_id","created_at",)

class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("user_id", "created_at", "body",)

class QualityAPI(ModelSerializer):
    class Meta:
        model = Quality
        fields = ("pk","cat",'photo',"name",)

class PaletSerializer(ModelSerializer):
    class Meta:
        model = Palet
        fields = ("pk",'name','char','photo')


class CharakterSerializer(ModelSerializer):
    class Meta:
        model = Charakter
        fields = ('name','pile','pile_height','yarn_weight','primary_basic','secondary_basic','points','total_weight')

class DesignSerializer(ModelSerializer):
    class Meta:
        model = Design
        fields = ("__all__")

class ProductAPI(ModelSerializer):
    class Meta:
        model = Product
        fields = ("__all__")
        read_only_fields = ("design",)
        depth = 3
