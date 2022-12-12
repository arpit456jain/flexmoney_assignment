from django.urls import path
from application_form import views


urlpatterns = [
    path("",views.application_form),
    path("user/",views.already_registered_user),
    path('submitform/', views.Application_formView.as_view(), name='submit'),
    path('submituser/', views.Alredy_registered_userView.as_view(), name='already_registered'),
]