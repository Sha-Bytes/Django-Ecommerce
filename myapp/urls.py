from django .urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login,name='login'),
    path('view/', views.view,name='view'),
    path('payment/', views.payment.as_view(), name='payment'),
    path('charge/', views.charge, name='charge'),
    path('signup/', views.signup, name='signup'),
    path("contact/", views.feedback, name="contact"),
    path("checkout/", views.checkout, name="checkout"),
]