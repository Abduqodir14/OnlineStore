from django.shortcuts import render
from .forms import SubsctiberForm


def landing(request):
    form = SubsctiberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['name'])
        print(form)

        new_form = form.save()
    return render(request, 'landing/landing.html', locals())
