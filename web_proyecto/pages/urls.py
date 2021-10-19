from django.urls import path
from .views import PageListView, PageDetalView, PageCreate, PageUpdate, PageDelete, PageCreateCategoria, PageCreateVideo

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetalView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('createcategoria/', PageCreateCategoria.as_view(), name='createcategoria'),
    path('createvideo/', PageCreateVideo.as_view(), name='createvideo'),
    path('update/<int:pk>', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>', PageDelete.as_view(), name='delete'),
], 'pages')