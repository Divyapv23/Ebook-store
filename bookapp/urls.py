from django.urls import path
from bookapp import views

urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('categorypage/', views.categorypage, name="categorypage"),
    path('categorydetails/', views.categorydetails, name="categorydetails"),
    path('catedisplaypage/', views.catedisplaypage, name="catedisplaypage"),
    path('editcatepage/<int:dataid>', views.editcatepage, name="editcatepage"),
    path('updatecatepage/<int:dataid>', views.updatecatepage, name="updatecatepage"),
    path('delcatepage/<int:dataid>', views.delcatepage, name="delcatepage"),
    path('productpage/', views.productpage, name="productpage"),
    path('productdetails/', views.productdetails, name="productdetails"),
    path('pdtdispage/', views.pdtdispage, name="pdtdispage"),
    path('editpdtpage/<int:dataid>', views.editpdtpage, name="editpdtpage"),
    path('updatepdtpage/<int:dataid>', views.updatepdtpage, name="updatepdtpage"),
    path('delpdt/<int:dataid>', views.delpdt, name="delpdt"),
    path('displaycart/', views.displaycart, name="displaycart")

]
