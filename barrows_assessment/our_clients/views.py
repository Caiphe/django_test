from django.shortcuts import render, redirect
from .models import Clients, Projects
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .forms import ClientsForm
from django.http import HttpResponseRedirect


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


#  This is the welcome Page
def home(request):
    return render(request, 'our_clients/home.html', {'title': 'Welcome-Home'})


#  The below function gets the list of all the clients and prevent the user that is
#  not logged in to access this page. We make use of login decorator
@login_required
def OurClients(request):
    context = {
        "clients": Clients.objects.all().order_by('-date_posted')
    }
    return render(request, 'our_clients/our_clients.html', context)


# This is the class based View that pulls the list of our clients
class ClientsListView(ListView):
    model = Clients
    template_name = 'our_clients/our_clients.html'
    context_object_name = 'clients'
    ordering = ['-date_posted']


# This View displays all the Projects logged against a single client
class ClientsDetailView(DetailView):
    model = Clients
    template_name = 'our_clients/client_detail.html'

    def get_context_data(self, **kwards):
        context = super(ClientsDetailView, self).get_context_data(**kwards)
        context['project_list'] = Projects.objects.all().order_by(
            'project_name')
        return context


# I'm using the Login Mixin to prevent users to access this page before siging in
class ClientsCreateView(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Clients
    fields = ["client_name", "contact_person", "contact_number"]

    def form_valid(self, form):
        return super().form_valid(form)


# This is the Update Class Based View
class ClientsUpdateView(LoginRequiredMixin, UpdateView):
    model = Clients
    fields = ["client_name", "contact_person", "contact_number"]

    def form_valid(self, form):
        return super().form_valid(form)


#  This is the client delete View
class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Clients
    success_url = '/'


#  This Functions Gets the list of all logged Projects ordered by the clients Name
@login_required
def GetLoggedProjects(request):
    context = {
        "Projects": Projects.objects.all().order_by('client_name')
    }
    return render(request, 'our_clients/projects_list.html', context)


# This is to log the project to aparticular Client Using
#  Mixin to check if The user is logged in if not redirect to Login Page
class LogProject(LoginRequiredMixin, CreateView):
    model = Projects
    fields = ["project_name", "project_status", "client_name"]
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


#  This is the Project delete View
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Projects
    success_url = '/'


#  This is the view that updates the project logged. Here We can only update the project name and the project staus
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Projects
    fields = ["project_name", "project_status"]
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)
