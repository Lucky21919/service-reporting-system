from django.shortcuts import render

# Create your views here.from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report

def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_reports')
    else:
        form = ReportForm()

    return render(request, 'create_report.html', {'form': form})


def view_reports(request):
    reports = Report.objects.all()
    return render(request, 'view_reports.html', {'reports': reports})
