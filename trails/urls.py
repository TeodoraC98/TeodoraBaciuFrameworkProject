from django.urls import path
from .views import (
    TrailListView, 
    TrailCreateView, 
    TrailDetailView, 
    TrailUpdateView,
    TrailDeleteView,
    bad_request,
)
from .import views

urlpatterns = [
    path('trail/<int:pk>', TrailDetailView.as_view(), name='trail-detail'),
    path('rout/new/',TrailCreateView.as_view(), name='trail-create'), 
    path('trail/<int:pk>/update/', TrailUpdateView.as_view(), name='trail-update'),
    path('trail/<int:pk>/delete/', TrailDeleteView.as_view(), name='trail-delete'),
    path('trail/bad_request/',views.bad_request, name='bad_request'),
    path('trail/join/',views.join, name='join'),
    path('trail/add_comment',views.add_comment, name='add_comment'),
]