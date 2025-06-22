from rest_framework import serializers
from carapp.models import ( Banner, Product, Category, Basket, Service, Marka,
                Advantages, Look, Mission, Media, Form, Order, SiteSettings 
)
from carapp.models import CustomUser
from django.contrib.auth.password_validation import validate_password


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = CustomUser
        fields = ("username", "password")
        
        
    def validate(self, data):
        validate_password(data["password"])
        return data
    
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        
        user = CustomUser.objects.create_user(
            username = username,
            password = password
        )
        return user
    
    
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields= '__all__'
        
                
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = "__all__"
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'image', 'name', 'price',)
        
        
class ProductRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
        
class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = ( 'image', 'name', 'price',)
        
        
class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = "__all__"
        
        
class LookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Look
        fields = "__all__"
        
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
        
        
class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = "__all__"
        
        
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"
        
        
class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"
        
        
class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"
        
        
class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"
        
        
class BasketRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"
        
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        