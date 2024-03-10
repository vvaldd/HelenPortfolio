from django.urls import path

from apps.albums.views import AlbumsListCreateView, AlbumsRetrieveUpdateDestroyView, AlbumListCreatePicturesView

urlpatterns = [
    path('', AlbumsListCreateView.as_view(), name='list_create_albums'),
    path('/<int:pk>', AlbumsRetrieveUpdateDestroyView.as_view(), name='retrieve_update_destroy_albums'),
    path('/<int:pk>/pictures', AlbumListCreatePicturesView.as_view(), name='list_create_album_pictures')
]
