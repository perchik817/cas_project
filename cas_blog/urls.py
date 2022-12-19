from django.urls import path
from . import views

app_name = 'cas'

urlpatterns = [
    path('main_page/', views.elems_view, name='main_page'),
	path('register/', views.register_request, name='register'),
	path('order/', views.order_view, name='order'),
	path('add_order/', views.add_order_view, name='add_order'),
	path('about_us', views.about_us_view, name='about_us'),
	path('elems_1_detail/<int:id>/', views.elems_1_detail_view, name='elems_detail'),
	path('elems_2_detail/<int:id>/', views.elems_2_detail_view, name='elems_detail'),
	path('elems_3_detail/<int:id>/', views.elems_3_detail_view, name='elems_detail'),
	path('elems_4_detail/<int:id>/', views.elems_4_detail_view, name='elems_detail'),
	]