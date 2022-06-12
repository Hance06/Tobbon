from sys import api_version
from django.urls import path
from tobbon.api import views as api_views

app_name='tobbon'

urlpatterns = [
    path('belgeler/', api_views.belge_list_create_api_view, name="belge-listesi"),
    path('belgeler/<int:pk>',api_views.belge_detail_api_view,name='belge-detay')

]