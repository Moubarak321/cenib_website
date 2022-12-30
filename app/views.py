from django.shortcuts import render, get_object_or_404
from app.models import Cours, Favorite, Formateur
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def index(request):
    formations = Cours.objects.all()
    favorites = Favorite.objects.all()
    formateursIn = Formateur.objects.filter(onIndex = True)
    return render(request, 'app/index.html', context={"formations":formations , 'favorites':favorites, 'formateursIn':formateursIn})

def about(request):
    formations = Cours.objects.all()
    return render(request, 'app/about.html', context={"formations":formations})

def courses(request):
    cours = Cours.objects.all()
    formations = Cours.objects.all()
    return render(request, 'app/courses.html', context={"cours":cours, "formations":formations})

def trainers(request):
    formations = Cours.objects.all()
    formateurs = Formateur.objects.all()
    return render(request, 'app/trainers.html', context={"formations":formations, 'formateurs':formateurs})

def pricing(request):
    formations = Cours.objects.all()
    return render(request, 'app/pricing.html', context={"formations":formations})

def events(request):
    formations = Cours.objects.all()
    return render(request, 'app/events.html', context={"formations":formations})



def contact(request):
    formations = Cours.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form_data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message,
        }

        message = '''
        From:\n\t\t{}\n
        Email:\n\t\t{}\n
        Subject:\n\t\t{}\n
        Message:\n\t\t{}\n
        '''.format(form_data['name'], form_data['email'],form_data['subject'] ,form_data['message'] )
        send_mail('You got a mail!', message, '', [settings.EMAIL_HOST_USER]) 

        messages.success(request, "Votre message a été envoyé avec succes !!")
        return render(request, 'app/contact.html')
    return render(request, 'app/contact.html', context={"formations":formations})



def course_details(request, id):
    cours = get_object_or_404(Cours, id=id)
    formations = Cours.objects.all()
    # return render (request, 'store/detail.html', context={"product": product} )
    return render(request, 'app/course-details.html', context={"cours": cours, "formations":formations})


# =========================
# another way to do
# =========================

# from django.shortcuts import render, redirect
# from .forms import ContactForm
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse


# # Create your views here.
# def homepage(request):
# 	return render(request, "main/home.html")

# def contact(request):
# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 			subject = "Website Inquiry" 
# 			body = {
# 			'first_name': form.cleaned_data['first_name'], 
# 			'last_name': form.cleaned_data['last_name'], 
# 			'email': form.cleaned_data['email_address'], 
# 			'message':form.cleaned_data['message'], 
# 			}
# 			message = "\n".join(body.values())

# 			try:
# 				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
# 			except BadHeaderError:
# 				return HttpResponse('Invalid header found.')
# 			return redirect ("main:homepage")
      
# 	form = ContactForm()
# 	return render(request, "main/contact.html", {'form':form})