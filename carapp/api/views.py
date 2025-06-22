from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from carapp.models import ( Banner, Product, Category, Product, Marka, Service, Advantages, Look, Mission, Form,
    Media, Order, SiteSettings, Basket
)
from carapp.models import CustomUser


from carapp.api.serializers import ( BannerSerializer , MarkaSerializer, AdvantagesSerializer,
    CategorySerializer, ProductSerializer,SiteSettingsSerializer, LookSerializer, MissionSerializer, FormSerializer,
    BasketSerializer, UserCreateSerializer,ServiceSerializer,MediaSerializer, SiteSettingsSerializer, OrderSerializer,
    ProductSerializer
)



class UserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    
    
class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    
    
   
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
    
class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"
    
    
class MarkaListAPIView(ListAPIView):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializer
    
    
class AdvantagesListAPIView(ListAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer
    
    
class LookListAPIView(ListAPIView):
    queryset = Look.objects.all()
    serializer_class = LookSerializer
    
    
class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    
class MissionListAPIView(ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    
    
class FormListAPIView(ListAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    
    
class MediaListAPIView(ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    
    
class SiteSettingsListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    
    
class BasketListAPIView(ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    
    
class BasketRetrieveAPIView(ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    lookup_field = "id"
    
    
class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    

    