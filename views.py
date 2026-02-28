from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomUserCreationForm, CreateReport
from .models import Report


from django.contrib.auth.decorators import login_required

# Create your views here.


def registerpage(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('loginpage')
        else:
            # Show form errors to user
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            
    context = {'form' : form}
    return render(request, 'accounts/register.html', context)




def loginpage(request):
    if request.user.is_authenticated:
        return redirect('submit_report')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
     
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('submit_report')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'accounts/login.html')
        
    return render(request, 'accounts/login.html')



# def loginpage(request):
#     print("Login view accessed")  # Debugging line
    
#     if request.user.is_authenticated:
#         print("User already authenticated, redirecting")  # Debugging line
#         return redirect('submit_report')

#     if request.method == 'POST':
#         print("POST request received")  # Debugging line
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(f"Auth attempt for: {username}")  # Debugging line

#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             print("Authentication successful")  # Debugging line
#             login(request, user)
#             messages.success(request, f'Welcome back, {username}!')
#             print(f"Redirecting to: {reverse('submit_report')}")  # Debugging line
#             return redirect('submit_report')
#         else:
#             print("Authentication failed")  # Debugging line
#             messages.error(request, 'Invalid username or password')
#             return render(request, 'accounts/login.html')
    
#     print("Rendering login template")  # Debugging line
#     return render(request, 'accounts/login.html')


# @never_cache  # Prevents browser caching of the logout page
# @csrf_protect  # Protects against CSRF attacks
# def logoutuser(request):
#     if request.method == 'POST':  # Only allow POST requests for logout
#         logout(request)
#         messages.success(request, 'You have been successfully logged out.')
#         return redirect('loginpage')
    
#     # If not POST, redirect to home or login page
#     return redirect('loginpage')


def test(request):
    return HttpResponse("<h1>Hello World</h1>")

@login_required # put this above every view that you want logged in
def submit_report(request):
    if request.method == "POST":
        model = Report
        form_class = CreateReport

        form = CreateReport(request.POST)

        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.save()
            messages.success(request, "Report submitted successfully!") 
            return redirect('submit_report')
    else:
        form = CreateReport()
        
    return render(request, 'accounts/submit.html', {"form" : form})



@login_required
# def user_reports(request):
#     user_reports = Report.objects.filter(created_at=request.user).order_by('-created_at')

#     reports_list = []
#     for report in user_reports:
#         reports_list.append({
#             'id': report.id,
#             'issue_type': report.get_issue_type_display(),
#             'created_at': report.created_at, 
#             'status': report.get_status_display()
#         })

#     return render(request, 'reports/user_reports.html', {
#         'reports': reports_list
#     })


def user_previous_reports(request):
    reports = Report.objects.filter(reporter=request.user).order_by('-created_at').values(
        'id',
        'location',
        'department',
        'issue_type',
        'created_at'
    )
    
    context = {
        'reports': reports,
        'total_reports': reports.count()
    }
    
    return render(request, 'accounts/user_previous_reports.html', context)




# return render(request, '//.html', { 'form' : form})