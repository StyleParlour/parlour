from django.urls import path
from . import views
# import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.analytics, name='analytics'),
    path('admin/offers/', views.offers, name='offers'),
    path('admin/frequency/', views.frequency, name='frequency'),
    path('admin/invoice/', views.invoice, name='invoice'),
    path('admin/slots/', views.slots, name='slots'),
    path('admin/products/', views.products, name='products'),
    path('admin/offers/delete/<int:id>', views.delete, name='delete'),
    path('admin/products/delete/<int:id>', views.deletePro, name='delete'),
    path('shop/', views.shop, name='shop'),
    path('slot/', views.slot, name='slot'),
    path('otp/', views.otp, name='otp'),
    path('invoiceGen/<int:id>', views.invoiceGen, name='invoiceGen'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)