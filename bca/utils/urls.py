from django.urls import path
from . import views

APP_NAME = 'utils'

urlpatterns = [
    path('', views.home, name='home'),
    path('notice/', views.notice, name='notice'),
    path('about/', views.about, name='about'),
    path('resource/', views.resource, name='resource'),
    path('contact/', views.contact, name='contact'),
    path('bqtbsbboeojspk/', views.login_user, name='login'),
    path('message/<int:id>/', views.get_hod_message, name='message'),
    path('notice/filter/<str:key>/', views.notice_filter, name='notice_filter'),
    path('logout/', views.logout_user, name='logout'),

    # for admin
    path('admin/', views.admin_home, name='admin'),
    path('admin_notice/', views.admin_notice, name='admin_notice'),
    path('admin_about/', views.admin_about, name='admin_about'),
    path('admin_resource/', views.admin_resource, name='admin_resource'),
    path('admin_contact/', views.admin_contact, name='admin_contact'),

    path('admin_notice/delete/<int:id>/', views.admin_notice_delete, name='admin_notice_delete'),
    path('admin_notice/edit/<int:id>/', views.admin_notice_edit, name='admin_notice_edit'),

    path('admin_home/hodmessage/update/<int:id>/', views.admin_HODmessage_update, name='admin_HODmessage_update'),
    path('admin_home/banner_imaage/update/<int:id>/', views.admin_banner_image_update, name='admin_banner_image_update'),


    path('admin_resource/delete/<int:id>/', views.admin_resource_delete, name='admin_resource_delete'),
    path('admin_resource/edit/<int:id>/', views.admin_resource_edit, name='admin_resource_edit'),

    path('admin_notice/filter/<str:key>/', views.admin_notice_filter, name='admin_notice_filter'),
]