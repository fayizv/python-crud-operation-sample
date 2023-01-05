from itertools import product
from multiprocessing import context
from unittest import result
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from .forms import NewUserForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages,auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . forms import EditProfileForm
from . forms import UserProfileInfo
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

@login_required(login_url='login')
def home(request):
    product = Product.objects.all()
    return render(request,'index.html',{'Products':product})

def register(request):
	form = NewUserForm()
	if request.method == "POST":
		
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			# login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('login')
		else :
			messages.error(request, "Unsuccessful registration. Invalid information.")
	

		context = {
		'form' : form ,
		}
		return render (request,'register.html',context)
	return render (request,'register.html')


def user_login(request):
	if 'user' in request.session:
		return redirect('home')
	elif 'admin' in request.session:
		return redirect('admin_dashboard')

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(request,username=username, password=password)
		
		if user is not None:
			if user.is_superuser:
				request.session['admin'] = username
				auth.login(request,user)
				messages.info(request, "You are now logged in as .")
				return redirect('admin_dashboard')

			else:
				request.session['user'] = username
				auth.login(request,user)
				return redirect('home')
		else:
			messages.error(request,"Invalid username or password.")
	else:
		messages.error(request,"Invalid username or password.")
	

	# context={
	# 	"login_form":form
	# }
	return render(request, 'login.html')


def user_logout(request):
		logout(request)
		messages.info(request, "You have successfully logged out.") 
		return redirect('login')


def admin_dashboard(request):
	users=User.objects.filter()

	context={
		'users' :users,
	}
	return render(request,'admin/admin.html',context)


def edit_profile(request,id):
	user =User.objects.get(pk=id)
	if request.method == 'POST':
		form = EditProfileForm(request.POST,instance= user,)

		if form.is_valid():
			user = form.save()
			user.save()
			return redirect(admin_dashboard)
	else:
		form = EditProfileForm()
	return render(request, "admin/edit.html", {'form':form,'user':user})


def delete(request,id):
    account = User.objects.get(id=id)
    account.delete()
    messages.success(request,'User deleted Successfully')
    return redirect(admin_dashboard)


def add_user(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'user added')
			return redirect(admin_dashboard)
	else:
		form = NewUserForm()
	
	context={
		'form' : form,
	}

	return render(request,'admin/add_user.html',context)

def search(request):
	if request.method == "POST" :
		keyword = request.POST.get('username') if request.POST.get('username') != None else ''
		results = User.objects.filter(username__istartswith=keyword)
		return render(request,'admin/admin.html',{"results":results})

	return render(request,'admin/admin.html')		