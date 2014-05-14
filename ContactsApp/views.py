from django.http import *
from django.shortcuts import render
from django import forms
from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from ContactsApp.models import *
import datetime


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")		

@login_required	
def profile(request):
	context = {}
	return render(request, 'templates/profile.html', context)	
	
		
		
def frontPage(request):
	t = ContactRepo()
	list = t.getAll()

	context = {"contacts": list}
	return render(request, 'templates/index.html', context)	

def newContact(request):	
	r = Contact()
	r.id = 0
	r.contact_date = datetime.datetime.now()
	context = {"contact" : r }
	return render(request, 'templates/editContact.html', context)

	
def editContact(request):
	id = request.GET["id"]	
	t = ContactRepo()
	r = t.get(id)	
	context = {"contact" : r }
	return render(request, 'templates/editContact.html', context)

def deleteContact(request):
	id = request.GET["id"]
	t = ContactRepo()
	r = t.delete(id)
	return HttpResponseRedirect("/")

def saveContact(request):
	t = ContactRepo()
	
	currentID = request.POST["id"]
	if(currentID == "0" or currentID == "None"):
		print("new")
		r = Contact()
		r.id = None
	else:
		print("update")
		r = t.get(currentID)
		
	r.first_name = request.POST["first_name"]
	r.last_name = request.POST["last_name"]
	r.email = request.POST["email"]
	r.company = request.POST["company"]
	r.notes = request.POST["notes"]
	r.age = toInt(request.POST["age"])
	r.contact_date = request.POST["contact_date"]

	try:
		if(currentID == "0" or currentID == "None"):
			t.add(r)
		else:
			t.update(r)

		return HttpResponseRedirect("/")
		
	except ValidationException as ve:
		context = {"contact" : r, "errors": ve.errors }
		return render(request, 'templates/editContact.html', context)
		
	
	
	
	