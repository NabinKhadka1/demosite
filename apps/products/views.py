from django.shortcuts import render
from .forms import CreateProductForm
from django.http import HttpResponseRedirect
from django.views import View


# Create your views here.
def create_form(request):
    form = CreateProductForm()
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid:
            form.save()

    return render(request,'backend/create_update/create.html',{'create_form':form})

class CreateProduct(View):
    form_class = CreateProductForm
    initial = {}
    template_name = 'backend/create_update/create.html'

    def get(self,request):
        form = self.form_class(initial = self.initial)
        return render(request,self.template_name,{'create_form':form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        return render(request,self.template_name,{'create_form':form})

