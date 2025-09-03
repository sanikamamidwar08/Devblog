from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),   # Home page -> All posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Post detail
    path('contact/', views.contact, name='contact'),  # Contact form
    path('contact/success/', views.contact_success, name='contact_success'),  # Success page
]
