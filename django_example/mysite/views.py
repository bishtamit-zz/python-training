from django.shortcuts import render

from .forms import AboutForm


def index(reqeust):
    return render(reqeust, 'index.html', {})


def about(request):
    form = AboutForm(request.POST or None)

    final_message = ""
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            contact = form.cleaned_data.get('contact')
            final_message = f'Thanks for subscribing. you will get weekly update on {email}/{contact}'
            # form = AboutForm()

    return render(request, 'about.html', {'form': form, 'final_message': final_message})
