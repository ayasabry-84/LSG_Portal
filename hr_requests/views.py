from django.shortcuts import render, redirect
from .forms import HRRequestForm
from .models import HRRequest, REQUEST_TYPES

def request_options_view(request):
    return render(request, 'hr_requests/request_options.html', {'types': REQUEST_TYPES})

def make_request_view(request, request_type):
    if request.method == 'POST':
        form = HRRequestForm(request.POST)
        if form.is_valid():
            hr_request = form.save(commit=False)
            hr_request.request_type = request_type
            hr_request.save()
            return render(request, 'hr_requests/success.html', {'request_type': dict(REQUEST_TYPES)[request_type]})
    else:
        form = HRRequestForm()
    return render(request, 'hr_requests/request_form.html', {'form': form, 'request_type': dict(REQUEST_TYPES)[request_type]})
