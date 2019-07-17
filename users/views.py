from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
    )

from .forms import (

    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm
    )
from .models import Profile


class Register(View):

    template_name = 'users/register.html'
    form = UserRegisterForm()
    ctx = {
        'form' : form,
        'title': 'Register'
    }

    def get(self,request,*args,**kwargs):
        return render(request,template_name=self.template_name, context=self.ctx)

    def post(self,request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Hey {} ! Your account has been created. Please Login to continue.'.format(username))
            return redirect('blog-home')


        return render(request,template_name=self.template_name, context=self.ctx)

class Profile(ListView):

    template_name = 'users/profile.html'







    def get_queryset(self):
        pass


    def get_context_data(self, **kwargs):
        context = super(Profile,self).get_context_data(**kwargs)
        context['title'] = 'Profile'
        return context





class ProfileUpdate(View):
    template_name = 'users/profile_edit.html'

    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()
        ctx = {
            'u_form': u_form,
            'p_form': p_form,

            'title': 'profile-update'
        }

        return render(request, template_name=self.template_name, context=ctx)

    def post(self,request,*args,**kwargs):
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Your account has been Updated.")
            return redirect('blog-profile',username= request.user.username)


