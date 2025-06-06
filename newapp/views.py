from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Company, ActivityTheme
from .forms import CompanyForm

def company_list(request):
    search_query = request.GET.get('q', '')
    priority_filter = request.GET.get('priority', '')
    region_filter = request.GET.get('region', '')
    activity_filters = request.GET.getlist('activity')
    
    companies = Company.objects.all().distinct()
    all_activities = ActivityTheme.objects.all().order_by('name')
    
    if search_query:
        companies = companies.filter(
            Q(name__icontains=search_query) | 
            Q(short_name__icontains=search_query) |
             Q(additional_contacts__icontains=search_query)
        )
        
    
    if priority_filter and priority_filter.isdigit() and 1 <= int(priority_filter) <= 10:
        companies = companies.filter(priority=int(priority_filter))
    
    if region_filter:
        companies = companies.filter(region=region_filter)
    
    if activity_filters:
        companies = companies.filter(activity_themes__id__in=activity_filters).distinct()
    
    paginator = Paginator(companies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'company_list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'priority_filter': priority_filter,
        'region_filter': region_filter,
        'activity_filters': [int(a) for a in activity_filters],
        'regions': Company.REGION_CHOICES,
        'priority_range': range(1, 11),
        'all_activities': all_activities,
    })

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Компания успешно добавлена')
                return redirect('company_list')
            except ValidationError as e:
                for field, errors in e.message_dict.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
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
            try:
                form.save()
                messages.success(request, 'Компания успешно обновлена')
                return redirect('company_list')
            except ValidationError as e:
                for field, errors in e.message_dict.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
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
        messages.success(request, 'Компания успешно удалена')
        return redirect('company_list')
    return render(request, 'company_confirm_delete.html', {
        'company': company
    })