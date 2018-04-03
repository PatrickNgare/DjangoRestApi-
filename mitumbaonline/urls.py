from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^api/products/$', views.ProductList.as_view()),
   url(r'^api/categories/$', views.CategoryList.as_view())
]
