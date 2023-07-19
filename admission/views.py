from django.shortcuts import render
from .forms import StudentForm

# Create your views here.

def index(req):
    form = StudentForm()
    return render(req, 'admission/index.html', {'form': form})