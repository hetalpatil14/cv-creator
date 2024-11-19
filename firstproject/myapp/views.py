from django.shortcuts import render,redirect,get_object_or_404
# from django.http import HttpResponse
from . models import Person
# from myproject.myapp.models import Person
# Create your views here.
# def index(request):
    # return HttpResponse("Hello there!")

def data(request):
    myapp = Person.objects.all()
    return render(request,'myapp/data.html',{'myapp':myapp})

def edit(request,pk):
    person= get_object_or_404(Person,pk=pk)
    return render(request,'myapp/edit.html',{'person':person})


def viewdata(request,pk):
    person= get_object_or_404(Person,pk=pk)
    return render(request,'myapp/vdata.html',{'person':person})

def register(request,pk):
    person= get_object_or_404(Person,pk=pk)
    return render(request,'myapp/register.html',{'person':person})

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        number = request.POST['number']
        email = request.POST['email']
        age = request.POST['age']
        objective = request.POST['objective']
        qualification = request.POST['qualification']
        skills = request.POST['skills']
        experience = request.POST['experience']
        honor= request.POST['honor']
        activity= request.POST['activity']
        service= request.POST['service']
        image = request.FILES['image']
        Person.objects.create( service=service,image=image,activity=activity,honor=honor,objective=objective,experience=experience,name=name,email=email,qualification=qualification,address=address,skills=skills,number=number,age=age)     
        return redirect('data')
    return render(request,'myapp/register.html')

# adding data
# def viewdata(request):
#     data = Person.objects.all()
#     return render(request,'myapp/data.html',{'data': data})
    
    
# def editdata(request,id):
#     edata = Person.objects.filter(pk=id)
#     return render(request,'myapp/edit.html',{'edata': edata})

def update(request,pk):
    person = get_object_or_404(Person,pk=pk)
    if request.method == 'POST':
        person.name = request.POST['name'],
        person.email = request.POST['email'],
        person.save()     
        return redirect('data')
    return render(request,'myapp/edit.html',{'person':person})

def delete(request,pk):
    person = get_object_or_404(Person,pk=pk)
    person.delete()
    return redirect('data')



