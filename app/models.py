from django.db import models
from django.urls import reverse
# Create your models here.


# class Enseignant(models.Model):
#     nom = models.CharField(max_length=100)
#     thumbnail = models.ImageField(upload_to="enseigants", blank=True, null=True) 
#     description = models.TextField(null=True)
    
#     def __str__(self):
#         return self.nom

# class Cours(models.Model):
#     nom = models.CharField(max_length=100)
#     thumbnail = models.ImageField(upload_to="cours", blank=True, null=True) 
#     libele = models.TextField(max_length=500,blank=True, null=True)
#     enseignant = models.ManyToManyField(Enseignant)
#     description = models.TextField(max_length=1000)

#     def __str__(self):
#         return self.nom



les_choix = [
        ('Lana' , 'Lana'),
        ('Antonio' , 'Antonio'),
        ('Brandon' , 'Brandon'),
        ('Prince MENSAH' , 'Prince MENSAH'),
        ('Daniel ZOUNON' , 'Daniel ZOUNON'),
        ('Ansbert ABALLOT' , 'Ansbert ABALLOT'),
        ('Théodore BEHANZIN' , 'Théodore BEHANZIN'),
        ('Moubarak BENON' , 'Moubarak BENON')]

class Cours(models.Model):
    nom = models.CharField(max_length=100)
    coursthumbnail = models.ImageField(upload_to="cours", blank=True, null=True) 
    price = models.IntegerField(default=50000)
    libele = models.TextField(max_length=500,blank=True, null=True)
    description = models.TextField(max_length=1000)
    prof=models.CharField(choices=les_choix, max_length=50, default="")
    profimage = models.ImageField(upload_to="enseignants", blank=True, null=True)
    

    def __str__(self):
        return f"{self.nom}" 

    def get_absolute_url(self):
        return reverse("course_details", kwargs = {"id": self.id}) # nom de l'url "product" et un paramètre contenant le slug


class Favorite(models.Model):
    cours = models.OneToOneField(Cours, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cours.nom}"

class Formateur(models.Model):
    nom =models.CharField(choices=les_choix, max_length=50, default="")
    cours = models.ManyToManyField(Cours)
    profimage = models.ImageField(upload_to="enseignants", blank=True, null=True)
    description = models.TextField(max_length=1000)
    fontion = models.TextField(max_length=500)
    onIndex = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.nom}"



    