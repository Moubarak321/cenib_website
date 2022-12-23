from django.shortcuts import render, get_object_or_404
from app.models import Cours

# Create your views here.

def index(request):
    formations = Cours.objects.all()
    return render(request, 'app/index.html', context={"formations":formations})

def about(request):
    formations = Cours.objects.all()
    return render(request, 'app/about.html', context={"formations":formations})

def courses(request):
    cours = Cours.objects.all()
    formations = Cours.objects.all()
    return render(request, 'app/courses.html', context={"cours":cours, "formations":formations})

def trainers(request):
    formations = Cours.objects.all()
    return render(request, 'app/trainers.html', context={"formations":formations})

def pricing(request):
    formations = Cours.objects.all()
    return render(request, 'app/pricing.html', context={"formations":formations})

def events(request):
    formations = Cours.objects.all()
    return render(request, 'app/events.html', context={"formations":formations})

def contact(request):
    formations = Cours.objects.all()
    return render(request, 'app/contact.html', context={"formations":formations})

def course_details(request, id):
    cours = get_object_or_404(Cours, id=id)
    formations = Cours.objects.all()
    # return render (request, 'store/detail.html', context={"product": product} )
    return render(request, 'app/course-details.html', context={"cours": cours, "formations":formations})

    