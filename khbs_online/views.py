from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Program, User_info, SpecialProgram, User_course
from .forms import *

# Create your views here.

def programs(request):
    all_programs = Program.objects.all()
    special_programs = SpecialProgram.objects.all()

    context = {

        'all_programs':all_programs,
        'special_programs':special_programs,
    }
    return render(request, 'khbs-online/programs.html', context)



def signup(request):
    if request.user.is_authenticated:
        return redirect('online:profile', user=request.user)
    else:
        signupform = SignUpForm()
        if request.method == 'POST':
            signupform = SignUpForm(request.POST or None, request.FILES)
            if signupform.is_valid():
                user = signupform.save()

                #saving the info into the customized model
                user_password = signupform.cleaned_data.get('password1')
                user_img      = signupform.cleaned_data.get('profile_img')

                User_info.objects.create(
                    user=user, 
                    user_password=user_password, 
                    user_img=user_img
                )
                
                login(request, user)
                return redirect('online:profile', user=user)
            else:
                messages.success(request, 'Invalid form')
                return render(request, 'khbs-online/signup.html', context={
                    'signupform':signupform
                })
            
        context = {
            'signupform':signupform,
        }
        return render(request, 'khbs-online/signup.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST or None)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You have been logged in')
                    return redirect('home')
                else:
                    messages.success(request, 'User is not found. Check your details carefully')

                    return redirect('online:signin')
            else:
                messages.success(request, 'User is not found. Check your details carefully')
                return redirect('online:signin')
        else:
            return render(request, 'khbs-online/login.html', context={'form':form})
        


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out. Thank you')
    return redirect('online:signin')


@login_required
def profile(request, user):

    # Ensure the requested user matches the currently logged-in user
    if request.user.username != user:
        return HttpResponseForbidden("You are not allowed to access this profile.")
    
    user_info = User_info.objects.get(user__username=user)
    all_user_courses = User_course.objects.filter(user=request.user)
    
    if all_user_courses:
        user_courses = all_user_courses[0]
    else:
        user_courses = ''

    context = {
        'user_info':user_info,
        'user_courses': user_courses
    }
    
    return render(request, 'khbs-online/profile-page.html', context)



@login_required
def add_to_user_course(request, title):
    # Get the Program object based on the provided title
    program = Program.objects.get(title=title)

    # Check if the user already exists in the User_course model
    course_qs = User_course.objects.filter(user=request.user)
    if course_qs.exists():
        # If the user already exists, get the first User_course object
        course = course_qs[0]

        # Check if the user has a course with the same program id
        if course.courses.filter(id=program.id).exists():
            # If the course exists, display a success message and redirect
            messages.success(request, 'This program is already available in your course. \n Visit your profile to continue with the course')
            return redirect('online:programs')
        
        else:
            course.courses.add(program)
    else:
        course = User_course.objects.create(
            user = request.user,
            date = timezone.now()
        )

        course.courses.add(program)
        messages.success(request, 'New program added to your courses')
        return redirect('online:profile', user=request.user)
    
    return redirect('online:profile', user=request.user)



@login_required
def remove_from_user_course(request, title):
    # Get the Program object based on the provided title
    program = Program.objects.get(title=title)

    # Check if the user already exists in the User_course model
    course_qs = User_course.objects.filter(user=request.user)
    if course_qs.exists():
        # If the user already exists, get the first User_course object
        course = course_qs[0]

        # Check if the user has a course with the same program id
        if course.courses.filter(id=program.id).exists():
            # If the course exists, remove program from the user's courses
            messages.success(request, 'Program is removed from your courses. \n Visit your profile')
            course.courses.remove(program)
            return redirect('online:programs')




@login_required
def add_to_user_special_course(request, title):
    # Get the Program object based on the provided title
    special_program = SpecialProgram.objects.get(title=title)

    # Check if the user already exists in the User_course model
    course_qs = User_course.objects.filter(user=request.user)
    if course_qs.exists():
        # If the user already exists, get the first User_course object
        course = course_qs[0]

        # Check if the user has a special course with the same program id
        if course.special_courses.filter(id=special_program.id).exists():
            # If the special course exists, display a success message and redirect
            messages.success(request, 'This program is already available in your course. \n Visit your profile to continue with the course')
            return redirect('online:programs')
        
        else:
            course.special_courses.add(special_program)
    else:
        course = User_course.objects.create(
            user = request.user,
            date = timezone.now()
        )

        course.special_courses.add(special_program)
        messages.success(request, 'New program added to your courses')
        return redirect('online:profile', user=request.user)
    
    return redirect('online:profile', user=request.user)




@login_required
def remove_from_user_special_course(request, title):
    # Get the Program object based on the provided title
    special_program = SpecialProgram.objects.get(title=title)

    # Check if the user already exists in the User_course model
    course_qs = User_course.objects.filter(user=request.user)
    if course_qs.exists():
        # If the user already exists, get the first User_course object
        course = course_qs[0]

        # Check if the user has a course with the same program id
        if course.special_courses.filter(id=special_program.id).exists():
            # If the special course exists, remove special program from the user's special courses
            messages.success(request, 'Program is removed from your courses. \n Visit your profile')
            course.special_courses.remove(special_program)
            return redirect('online:programs')
        


@login_required
def course_series(request, id):
   # Check if the user has the course in User_course
    check_list = User_course.objects.filter(user=request.user)
    if not check_list.exists() or not check_list.filter(special_courses__id=id).exists():
        # If the user doesn't have the course, return forbidden response
        return HttpResponseForbidden("You do not have access to this page.")


    program = SpecialProgram.objects.get(id=id)
    program_series = program.video_series.all()

    context = {
        'program':program,
        'program_series':program_series,
    }
    return render(request, 'khbs-online/playlist.html', context)