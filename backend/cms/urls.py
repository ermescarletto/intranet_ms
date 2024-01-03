from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = 'cms'

urlpatterns = [
    path('campanha/list', BannerListView.as_view(), name='banner_list'),
    path('campanha/create/', BannerCampanhaCreateView.as_view(), name='create_campanha'),
    path('campanha/edit/<int:pk>', BannerCampanhaEditView.as_view(), name='edit_campanha'),
    path('campanha/remove/<int:pk>', BannerCampanhaDeleteView.as_view(), name='remove_campanha'),
    path('campanha/detail/<int:pk>', BannerCampanhaDetailView.as_view(), name='detail_campanha'),
]

