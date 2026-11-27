from django.urls import path
from .views import home_view, project_list_view, project_detail_view

urlpatterns = [
    path('', home_view, name = 'home'),
    path('projekty/', project_list_view, name = 'project_list'),
    path('projekty/<slug:slug>/', project_detail_view, name = 'project_detail')
]