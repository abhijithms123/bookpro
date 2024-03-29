from django.urls import path
from customer import views

urlpatterns = [
    path("home", views.CustomerIndex.as_view(), name="custhome"),
    path("accounts/register", views.SignUpView.as_view(), name="signup"),
    path("accounts/login", views.SignInView.as_view(), name="signin"),
    path("accounts/logout",views.signout, name="signout"),
    path("accounts/password/reset",views.PasswordResetView.as_view(),name="passwordreset"),
    path("cart/items/add/<int:id>",views.add_to_cart,name="addtocart"),
    path("cart/all",views.ViewMyCart.as_view(),name="mycart"),
]

