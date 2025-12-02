from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from .forms import DepartmentForm

# List all departments
def department_list(request):
    query = request.GET.get('q')  # Get search query from URL
    if query:
        department = Department.objects.filter(name__icontains=query)
    else:
        department = Department.objects.all()
    return render(request, 'department_list.html', {'department': department})

# Add new department
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', {'form': form})

# Edit department
def edit_department(request, id):
    dept = get_object_or_404(Department, id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=dept)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=dept)
    return render(request, 'edit_department.html', {'form': form})

# Delete department
def delete_department(request, id):
    dept = get_object_or_404(Department, id=id)
    if request.method == "POST":
        dept.delete()
        return redirect('department_list')
    return render(request, 'delete_department.html', {'department': dept})
