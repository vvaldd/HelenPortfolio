from django.urls import path

from .views import PicturesListCreateView, PicturesRetrieveUpdateDestroyView

urlpatterns = [
    path('', PicturesListCreateView.as_view(), name='list_create_pictures'),
    path('/<uuid:pk>', PicturesRetrieveUpdateDestroyView.as_view(), name='retrieve_update_destroy_pictures'),
]
