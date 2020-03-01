from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:result_id>/', views.result, name='result'),
    path('upload', views.model_form_upload, name='upload'),



]

