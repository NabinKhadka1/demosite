from django.shortcuts import render
from django.views.generic import FormView
from .forms import LoginForm

# Create your views here.
class CreateLoginForm(FormView):
    form_class = LoginForm
    template_name = 'backend/login_logout/login.html'

    
    def form_invalid(self,form):
        username = form.data.get('username')
        pass

    def form_valid(self,form):
        from django.contrib.auth import authenticate
        username = form.data.get['username']
        password = form.data.get['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return HttpResponseRedirect(self.request.META['HTTP_REFERER'])
        else:
            return HttpResponseRedirect(self.request.META['HTTP_REFERER'])
     



      
  
    
