from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def login(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password1"]

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect("/")
		else:
			messages.info(request,"Ingreso invalido")
			return redirect("login")
	else:
		return render(request,"login.html")

def logout(request):
	auth.logout(request)
	return redirect("/")

def registro(request):
	if request.method == "POST":
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		username = request.POST["username"]
		password1 = request.POST["password1"]
		password2 = request.POST["password2"]
		email = request.POST["email"]

		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,"El usuario ya existe")
				return redirect("registro")

			elif User.objects.filter(email=email).exists():
				messages.info(request,"El correo ya esta en uso")
				return redirect("registro")

			else:
				user = User.objects.create_user(
					first_name=first_name,
					last_name=last_name,
					username=username,
					password=password1,
					email=email,
				)
				user.save();
				return redirect("login")
		else:
			messages.info(request,"La clave no es igual")
			return redirect("registro")

	else:
		return render(request,"registro.html")