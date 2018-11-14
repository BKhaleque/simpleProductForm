from django.urls import path
from form import views

app_name = 'form'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('<int:product_id>/', views.product_details, name='detail'),
    path('', views.products, name='add'),
    path('data', views.products, name='data'),
    path('<int:product_id>/update/', views.products, name='update'),
]
