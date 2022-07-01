from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Download, Code

# Create your views here.
def index(req):
    return render(req, "index.html")

def beta(req):
    return render(req, 'beta.html')

@csrf_exempt
def getCode(req):
    if req.method == "POST":
        data = req.POST
        code = Code.objects.filter(code=data['code']).first()
        if code:
            Download(ip=data['ip'], country=data['country'], comment=code.comment).save()
            return JsonResponse({"success": True, "link": code.link})
        else:
            return JsonResponse({"success": False})

def route_all(req, path):
    return redirect("/")