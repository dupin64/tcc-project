from django.shortcuts import render


def index(request):
    if not request.user.id:
        return render(request, 'account/index.html', {})
    else:
        return render(request, 'home/index.html')
