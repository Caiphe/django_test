from django.urls import path, include
from .views import (
    ClientsDetailView,
    ClientsListView,
    ClientsCreateView,
    ClientsUpdateView,
    ClientDeleteView,
    LogProject,
    ProjectDeleteView,
    ProjectUpdateView,
    GetLoggedProjects
)
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('clients/new/', ClientsCreateView.as_view(), name="new-client"),
    path('clients/<int:pk>/update',
         ClientsUpdateView.as_view(), name="client-update"),
    path('clients/<int:pk>/delete',
         ClientDeleteView.as_view(), name="client-delete"),
    path('clients/project/<int:pk>/update',
         ProjectUpdateView.as_view(), name="project-update"),
    path('clients/project/<int:pk>/delete',
         ProjectDeleteView.as_view(), name="project-delete"),
    path('clients/', views.OurClients, name="clients"),
    path('logged-projects/', views.GetLoggedProjects, name="projects-list"),
    path('clients/<int:pk>/', ClientsDetailView.as_view(), name="client-detail"),
    path('clients/projects/', LogProject.as_view(), name="log-project"),
]
