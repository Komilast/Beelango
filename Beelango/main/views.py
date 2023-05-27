from django.shortcuts import render


def home(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, 'main/welcome.html')
    else:
        pass
