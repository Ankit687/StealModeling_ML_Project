from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from Alloy.models import User_Detail


# Create your views here.
def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        purpose = request.POST['purpose']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('/signup/')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('/signup/')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                user_detail = User_Detail(user=user, purpose=purpose)
                user.save()
                user_detail.save()
                print('user created')
                return redirect('/')

        else:
            messages.info(request, 'password not matching..')
            return redirect('/')

    else:
        return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid username')
            return redirect('/')

    else:
        return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
