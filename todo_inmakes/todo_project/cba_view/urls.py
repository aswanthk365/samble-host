from django.urls import path
from . import views

urlpatterns = [
    path('listView/',views.taksListView.as_view(),name='listView'),
    path('DeatilView/<int:pk>/',views.deatailView.as_view(),name='DeatailView'),
    path('updateview/<int:pk>/',views.updateview.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.cbvdelete.as_view(),name='deleteview'),


]
