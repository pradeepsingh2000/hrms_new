from django.shortcuts import render

# Create your views here.

def view_report(request):
    # Clear the breadcrumb history
    request.session['breadcrumbs'] = []
    return render(request, 'newReport/viewReport.html')
