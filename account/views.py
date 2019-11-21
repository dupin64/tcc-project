from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import redirect, render
from django.http.response import JsonResponse
from .models import Patient, Specialist

User = get_user_model()


def index(request):
    return render(request, 'account/index.html')


def sign_up(request):
    name = request.POST.get('name')
    user_type = request.POST.get('user_type')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.create(
        email=email,
        name=name,
        user_type=user_type
    )

    user.set_password(password)
    user.save()

    if user_type == 'patient':
        Patient.objects.create(user=user)
    elif user_type == 'specialist':
        Specialist.objects.create(user=user)

    return redirect('/', request)


def sign_in(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=email, password=password)
    if user:
        login(request, user)
        return redirect('/', request)
    return redirect('/', request)


def sign_out(request):
    logout(request)
    return redirect('/', request)


def search(request):
    keyword = request.GET.get('keyword')
    if not keyword:
        specialists = Specialist.objects.values('id', 'user__name', 'title')
    else:
        specialists = Specialist.objects.filter(user__name__contains=keyword).values('id', 'user__name', 'title')
    return JsonResponse({"success": True, "result": list(specialists)})
