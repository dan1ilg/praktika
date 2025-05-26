from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Company
from .forms import CompanyForm

def company_list(request):
    search_query = request.GET.get('q', '')
    priority_filter = request.GET.get('priority', '')
    region_filter = request.GET.get('region', '')
    
    companies = Company.objects.all()
    
    if search_query:
        companies = companies.filter(
            Q(name__icontains=search_query) | 
            Q(short_name__icontains=search_query)
        )
    
    if priority_filter and priority_filter.isdigit() and 1 <= int(priority_filter) <= 10:
        companies = companies.filter(priority=int(priority_filter))
    
    if region_filter:
        companies = companies.filter(region=region_filter)
    
    paginator = Paginator(companies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'company_list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'priority_filter': priority_filter,
        'region_filter': region_filter,
        'regions': Company.REGION_CHOICES,
        'priority_range': range(1, 11),  # Генерация чисел от 1 до 10
    })

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    
    return render(request, 'company_form.html', {
        'form': form,
        'title': 'Добавление компании'
    })

def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    
    return render(request, 'company_form.html', {
        'form': form,
        'title': 'Редактирование компании'
    })

def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, 'company_confirm_delete.html', {
        'company': company
    })