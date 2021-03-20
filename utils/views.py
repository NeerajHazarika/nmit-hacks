from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def try_to_login(request):
    username=request.GET.get("username",None)
    password=request.GET.get("password",None)
    if username==None or password==None:
        return render(None, "login-form.html")
    return HttpResponse("Yes")
    