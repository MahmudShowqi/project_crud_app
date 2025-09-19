from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from .models import Student
from .forms import StudentForm
def home(request):


    return render(request,'home.html')

def add_student(request):

    if request.method =='POST':

        student = StudentForm(request.POST)
        
        if student.is_valid():
            student.save()
        
        return redirect('home')

    else:

        form =StudentForm()

        return render(request,'add.html',{'form':form})
    

def student_list(request):

    try:
        students = Student.objects.all()
        return render(request,'list.html',{'students':students})
    
    except Student.DoesNotExist:

        return HttpResponse("no student is available")


