from django.urls import path
from carapp.api import views


urlpatterns = [
    path('user-create/', views.UserCreateAPIView.as_view()),
    
    path('banner-list/', views.BannerListAPIView.as_view()),
   
    path('category-list/',views.CategoryListAPIView.as_view()),

    path('product-list/',views.ProductListAPIView.as_view()),   
    path('product-retrieve/<int:id>/',views.ProductRetrieveAPIView.as_view()),

    path('marka-list/',views.MarkaListAPIView.as_view()),
    
    path('advantages-list/',views.AdvantagesListAPIView.as_view()),
    
    path('look-list/',views.LookListAPIView.as_view()),
    
    path('service-list/',views.ServiceListAPIView.as_view()),
      
    path('mission-list/',views.MissionListAPIView.as_view()), 
                           
    path('form-list/',views.FormListAPIView.as_view()),
    
    path('media-list/',views.MediaListAPIView.as_view()),
    
    path('sitesettings-list/',views.SiteSettingsListAPIView.as_view()),
    
    path('basket-list/', views.BasketListAPIView.as_view()),
     
    path('basket-retrieve/<int:id>/',views.BasketRetrieveAPIView.as_view()),
    
    path('order-list/',views.OrderListAPIView.as_view()),         
]