from django.shortcuts import render

# Create your views here.
import json
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Customer
from dbHandler import pgExecQuery,pgExecUpdate
# Create your views here.
@csrf_exempt
def register(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			user = User(username = reqdata["email"])
			user.set_password(reqdata["password"])
			user.save()
			customer = Customer()
			customer.user = user
			customer.save()
			return JsonResponse({"statuscode": "Registered Successfully"})
		except:
			return JsonResponse({"statuscode": "False"})

	if request.method == 'GET':
		pass

@csrf_exempt
def user_login(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			user = authenticate(username = reqdata["email"], password = reqdata["password"])
			if user:
				login(request, user)
				return JsonResponse({"status": True})
			return JsonResponse({"statuscode": "Invalid Credentials"})
		except:
			return JsonResponse({"statuscode": "False"})

	if request.method == 'GET':
		pass

@csrf_exempt
def user_logout(request):
	logout(request)
	return JsonResponse({"status": True})

@csrf_exempt
def contentupload(request):
	logout(request)
	return JsonResponse({"status": True})

@csrf_exempt
def markerdownload(request):
	logout(request)
	return JsonResponse({"status": True})
