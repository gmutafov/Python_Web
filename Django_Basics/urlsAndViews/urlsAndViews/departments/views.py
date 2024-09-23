from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from urlsAndViews.departments.models import Department


# Create your views here.


def index(request):
    url = reverse('redirect-view')
    url_lazy = reverse_lazy('redirect-view')
    return HttpResponse(f'<h1>{url_lazy}</h1>')


def view_with_name(request, variable):
    # return HttpResponse(f'<h1>Variable: {variable}</h1>')
    return render(request, 'departments/name_template.html', {"variable": variable})


def view_with_int_pk(request, pk):
    return HttpResponse(f"<h1>Int pk with pk: {pk}</h1>")


def view_with_slug(request, pk, slug):
    # department = Department.objects.filter(pk=pk, slug=slug)
    #
    # if not department:
    #     raise Http404

    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponse(f"<h1>Department from slug: {department}</h1>")


def redirect_to_softuni(request):
    return redirect('https://softuni.bg/')


def redirect_to_view(request):
    # return redirect(index)
    # return redirect('home')
    return redirect('numbers', pk=2)
