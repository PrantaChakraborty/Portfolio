from django.shortcuts import render
from .models import About, Experience, Education, Interest, Skill
# Create your views here.


def listView(request):
    about_display = About.objects.all()
    experience_display = Experience.objects.all()
    education_display = Education.objects.all()
    interest_display = Interest.objects.all()
    skill_display = Skill.objects.all()
    return render(request, 'base.html', {'About': about_display, 'Experience': experience_display,
                                         'Education': education_display, 'Interest': interest_display,
                                         'Skill': skill_display})


