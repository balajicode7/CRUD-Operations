from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import Employee
from .models import EmployeeModel

# Create your views here.
def show(request):
    if request.method == 'POST':
        data = Employee(request.POST)
        if data.is_valid():
            name = data.cleaned_data['name']
            email = data.cleaned_data['email']
            contact = data.cleaned_data['contact']
            password = data.cleaned_data['password']
            res = EmployeeModel(name=name,email=email,contact=contact,password=password)
            res.save()
            data = Employee()
    else:
        data = Employee()
    emp = EmployeeModel.objects.all()
    return render(request,"view.html",{'form':data,'em':emp})

def update(request,id):
    if request.method == 'POST':
        up = EmployeeModel.objects.get(pk=id)
        fo = Employee(request.POST,instance=up)
        if fo.is_valid():
            fo.save()
    else:
        up = EmployeeModel.objects.get(pk=id)
        fo = Employee(instance=up)
    return render(request,'update.html',{'form':fo})


def delete(request,id):
    if request.method == 'POST':
        de = EmployeeModel.objects.get(pk=id)
        de.delete()
    return redirect('show')


