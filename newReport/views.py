from django.shortcuts import render

# Create your views here.

def view_report(request):
    # Clear the breadcrumb history
    request.session['breadcrumbs'] = []
    return render(request, 'newReport/viewReport.html')

def dashboard(request):
    # First clear the session
    request.session.pop('breadcrumbs', None)
    # Set new breadcrumbs with only two levels

    return render(request, 'newReport/dashbord.html')

def category(request):
    request.session.pop('breadcrumbs', None)
    return render(request, 'newReport/category.html')

def create_category(request):
    request.session.pop('breadcrumbs', None)
    return render(request, 'newReport/createCategory.html')

