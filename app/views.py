from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.forms import URLForm
from app.models import URL


def homepage(request):
    return render(request, 'main.html')


def create_link(request):
    form = URLForm()
    if request.method == 'POST':
        form = URLForm(request.POST)
        if request.user.is_anonymous:
            if form.is_valid():
                form.save()
            context = {'form': form}
            return render(request, "create_link_for_anonym_user.html", context)
        if request.user:
            form.instance.owner = request.user
            form.instance.owner_id = request.user.id
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "createlink.html", context)


def all_links(request):
    links = URL.objects.all()
    context = {'links': links}
    return render(request, 'links.html', context=context)


@login_required
def get_my_links(request):
    user = request.user
    links = URL.objects.filter(owner__id=user.id)
    context = {'links': links}
    return render(request, "my_links.html", context)


