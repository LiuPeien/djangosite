from django.shortcuts import render
from django.http import JsonResponse
import json

def sqlsearch(request):
    return render(request, 'sqlsearch.html')

def hqlmanager(request):
    return render(request, 'hqlmanager.html')

def hqltasklist(request):
    return render(request, 'hqltasklist.html')

def execute(request):
    req = json.loads(request.body)
    print(req)
    print(type(req))
    return JsonResponse({"OK": 1})