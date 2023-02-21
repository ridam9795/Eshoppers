from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='ShopHome'),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path("login/", views.handlelogin, name="login"),
    path("signup/", views.handlesignup, name="signup"),
    path("logout/", views.handlelogout, name="logout"),
    path("checkout/logout/", views.handlelogout, name="checkoutlogout"),

]