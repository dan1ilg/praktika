from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Company
from .forms import CompanyForm

def company_list(request):
    search_query = request.GET.get('q', '')
    companies = Company.objects.filter(name__icontains=search_query) if search_query else Company.objects.all()
    
    paginator = Paginator(companies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'company_list.html', {
        'page_obj': page_obj,
        'search_query': search_query
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