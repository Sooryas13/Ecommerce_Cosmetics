from django.urls import path
from.import views

urlpatterns=[
    path('store/',views.store,name='store'),
    path('store/<slug:category_slug>/',views.store,name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail, name='product_detail'),
    path('search/',views.search,name='search'),
    path('about/',views.about,name='about')
]