from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from mainapp.views import *
from authapp.views import *


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),

    path('registration/', RegPageView.as_view(), name='registration'),
    path('auth/', AuthPageView.as_view(), name='auth'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('web-development/', WebPageView.as_view(), name='web'),
    path('mobile-development/', MobilPageView.as_view(), name='mobile'),
    path('marketing/', MarketingPageView.as_view(), name='marketing'),

    path('service/<int:pk>/detail/', ServiceDetailPageView.as_view(), name='service_detail'),

    path('order/', OrderPageView.as_view(), name='order'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('review/<int:pk>/', ReviewPageView.as_view(), name='review'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),

    # path('design/', DesignPageView.as_view(), name='design'),

    path('web-development/<int:pk>/detail/', MarketingDetailPageView.as_view(), name='web_detail'),
    path('mobile-development/<int:pk>/detail/', MobilDetailPageView.as_view(), name='mobile_detail'),
    path('marketing/<int:pk>/detail/', MarketingDetailPageView.as_view(), name='marketing_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
