from django.shortcuts import render, redirect
from .forms import StudentRegForm, ParentRegForm
from django.contrib import messages
from .models import *
# from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'khbs/home.html')

def admission1_reg(request):
    st_form = StudentRegForm()
    if request.method == 'POST':
        st_form = StudentRegForm(request.POST or None, request.FILES)
        if st_form.is_valid():
            st_form.save()
            #go to addmission2
            student_id = st_form.instance.id
            return redirect('register2', st_id=student_id)
        else:
            context = {
                'st_form':st_form,
            }
            messages.success(request, 'Form not valid')
            return render(request, 'khbs/admission1-reg.html', context)
        
    context = {
        'st_form':st_form,
    }
    return render(request, 'khbs/admission1-reg.html', context)



def admission2_reg(request, st_id):
    try:
        student = Student_reg.objects.get(pk=st_id)
    except Student_reg.DoesNotExist:
        messages.success(request, 'You have to register the student first before filling parent informations')
        return redirect('register1')
    
    parent_form = ParentRegForm()
    if request.method == 'POST':
        student = Student_reg.objects.filter(pk=st_id)[0]
        parent_form = ParentRegForm(request.POST or None, request.FILES)
        if parent_form.is_valid():
            parent_details = parent_form.save(commit=False)
            parent_details.student = student
            parent_details.save()
            messages.success(request, 'Complete registration with parent informations')
            return redirect('home')
        else:
            context = {
                'parent_form':parent_form,
            }
            messages.success(request, 'Form not valid')
            return redirect('register2', st_id=st_id)
        
    context = {
        'parent_form':parent_form,
    }
    return render(request, 'khbs/admission2-reg.html', context)


def about(request):
    return render(request, 'khbs/about.html')


def news_letter(request):
    if request.method == 'POST':
        email = request.POST['newsemail']
         
        email_queryset = NewsLetterEmail.objects.filter(email=email)
        if not email_queryset:
            NewsLetterEmail.objects.create(
                email=email
            )
            messages.success(request, 'Thanks for subscribing')
            return redirect('home')
        else:
            messages.success(request, 'Email already added')
            return redirect('home')