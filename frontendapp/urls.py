from django.urls import path
from frontendapp import views

urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('frontcatepage/<category>/', views.frontcatepage, name="frontcatepage"),
    path('singleproductpage/<int:dataid>', views.singleproductpage, name="singleproductpage"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('cartdetails/', views.cartdetails, name="cartdetails"),
    path('cartdelete/<int:dataid>', views.cartdelete, name="cartdelete"),
    path('cartadddetails/', views.cartadddetails, name="cartadddetails"),
    path('userpage/', views.userpage, name="userpage"),
    path('signuppage/', views.signuppage, name="signuppage"),
    path('customerlogin/', views.customerlogin, name="customerlogin"),
    path('weblogout/', views.weblogout, name="weblogout"),
]
