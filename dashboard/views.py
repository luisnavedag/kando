from django.shortcuts import render, redirect

# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        return redirect('user-dashboard')
    return render(request, "dashboard/dashboard.html")
