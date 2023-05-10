from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('addc',views.addc,name='addc'),
    path('addcdb',views.addcdb,name='addcdb'),
    path('adds',views.adds,name='adds'),
    path('addsdb',views.addsdb,name='addsdb'),
    path('show',views.show,name='show'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editdb/<int:pk>',views.editdb,name='editdb'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
]