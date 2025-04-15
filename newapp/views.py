from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm
import json

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.activity_themes = [x.strip() for x in request.POST['activity_themes'].split(',')]
            company.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'company_form.html', {'form': form})