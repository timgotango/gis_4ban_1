from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    if request.method == "POST": # request 안에 method라는 데이터가 POST 방식이라면,
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!'}) # key는 text, value에는 문장을 넣었다
    else: # GET 방식이라면,
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!'})