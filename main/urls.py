"""
URL 설정
"""
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('business/', views.business, name='business'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('notice/', views.notice_list, name='notice_list'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('estimate/', views.estimate_list, name='estimate_list'),
    path('estimate/create/', views.estimate_create, name='estimate_create'),
    path('estimate/<int:pk>/', views.estimate_detail, name='estimate_detail'),
    path('faq/', views.faq_list, name='faq_list'),
    path('faq/<int:pk>/', views.faq_detail, name='faq_detail'),
    path('pr/', views.pr_center, name='pr_center'),
    path('newsletter/', views.newsletter_list, name='newsletter_list'),
    path('newsletter/<int:pk>/', views.newsletter_detail, name='newsletter_detail'),
]

