from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
# Create your views here.

@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('view')
    else:
        initial_data = {'username':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 

def adlog_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dash')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 
@auth
def dashboard_view(request):
    return render(request, 'dashboard.html')
def quiz_view(request):
    return render(request, 'quiz.html')
def course_view(request):
    return render(request, 'course.html')
def program_view(request):
    return render(request, 'pro.html')
def short_view(request):
    return render(request, 'short.html')
def logout_view(request):
    logout(request)
    return redirect('login')



from django.shortcuts import render
import traceback
from io import StringIO
from contextlib import redirect_stdout  # Add this import
from django.http import HttpResponse
 
def execute_code(code):
    try:
        # Capture standard output in a buffer
        output_buffer = StringIO()
        with redirect_stdout(output_buffer):
            exec(code)
        output = output_buffer.getvalue()
    except Exception as e:
        # Provide detailed error information
        output = f"Error: {str(e)}\n{traceback.format_exc()}"
    return output
 
# def index(request):
#     return render(request, 'index.html')
 
def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST['codearea']
        output = execute_code(codeareadata)
        return render(request, 'program.html', {"code": codeareadata, "output": output})
    return HttpResponse("Method not allowed", status=405)