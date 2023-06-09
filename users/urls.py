from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),
    path('',views.home,name="home"),
    path('mentalhealthspecialists/',views.profiles,name="profiles"),
    path('profile/<str:pk>',views.userProfile,name='user-profile'),
    path('account/',views.userAccount,name='account'),
    path('edit-account/',views.editAccount,name='edit-account'),

    path('create-qualification/', views.createQualification, name="create-qualification"),
    path('update-qualification/<str:pk>/', views.updateQualification, name="update-qualification"),
    path('delete-qualification/<str:pk>/', views.deleteQualification, name="delete-qualification"),

    path('inbox/',views.inbox,name='inbox'),
    path('message/<str:pk>/',views.viewMessage,name='message'),
    path('create-message/<str:pk>/',views.createMessage,name='create-message'),

    path('create-appointment/<str:pk>/',views.createAppointment,name='create-appointment'),
    path('appointment/<str:pk>/',views.viewAppointment,name='appointment'),
    path('appointment-inbox/',views.appointmentInbox,name='appointmentInbox'),
    path('delete-appointment/<str:pk>/',views.deleteAppointment,name='deleteAppointment'),
    path('confirm-appointment/<str:pk>',views.confirmAppointment,name='confirmAppointment'),
    path('audiotherapy/',views.audiotherapy,name='audiotherapy'),
    path('readingtherapy/',views.readingtherapy,name='readingtherapy'),
    path('laughtherapy/',views.laughtherapy,name='laughtherapy'),
    path('yogatherapy/',views.yogatherapy,name='yogatherapy'),
    path('spiritualtherapy/',views.spiritualtherapy,name='spiritualtherapy'),
    path('childtherapy/',views.childtherapy,name='childtherapy'),
  
    
]
