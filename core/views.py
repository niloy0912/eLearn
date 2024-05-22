from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

from django.views import View
from .forms import *


# Create your views here.
class Home(View):
    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            context['username'] = request.user.username
        return render(request, 'core/home.html', context)
    
    def post(self, request):
        return render(request, 'core/home.html')
    
    
class Register(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.username = form.cleaned_data['username']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.set_password(form.cleaned_data['password1'])
                user_type = form.cleaned_data['user_type']
                if user_type == 'student':
                    user.is_student = True
                elif user_type == 'teacher':
                    user.is_teacher = True
                user.save()
                
                # print(user.password2)
                login(request, user)
                return redirect('home')  # Redirect to home page
            except IntegrityError:
                form.add_error('username', 'A user with that username already exists.')
        return render(request, 'registration/signup.html', {'form': form})


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('home')



# class LogIn(View):
#     def get(self, request):
        
#         print("login get called")
        
#         form = CustomAuthenticationForm()
#         # print(form.is_bound)
#         return render(request, 'registration/signup.html', {'form': form})

#     def post(self, request):
#         form = CustomAuthenticationForm(data=request.POST)
        
#         print("login post called")

#         # print(form.is_valid()) 
#         if form.is_valid():
#             print("form is valid")
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             print(username, password)
#             user = authenticate(request, username=username, password=password)
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         # print(form.errors)
        
#         return render(request, 'registration/signup.html', {'form': form})  
    
            
# def logout_1(request):
    # print("Logout called")
    # logout(request)
    # return redirect('home')