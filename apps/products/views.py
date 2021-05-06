from django.shortcuts import render
from .forms import CreateProductForm

# Create your views here.
def create_form(request):
    form = CreateProductForm()
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid:
            form.save()

    return render(request,'backend/create_update/create.html',{'create_form':form})
