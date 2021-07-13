from django.http import HttpResponse
from django.shortcuts import render
from accountapp.models import NewModel

def hello_world(request):
    if request.method == "POST": # request 안에 method라는 데이터가 POST 방식이라면,

        temp = request.POST.get('input_text') # request 안에 있는 POST 데이터 중, input_text 라는 이름을 가져와~~

        new_model = NewModel() # models.py의 NewModel 클래스 객체 생성
        new_model.text = temp # NewModel 안 text에 input한 것을 넣는 것.
        new_model.save() # 저장까지 해줘야!

        data_list = NewModel.objects.all()  # NewModel 데이터의 모든 값들
        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list}) # 최종적으로 저장된 것이 템플릿으로 넘어가는 것!!!
    else: # GET 방식이라면,
        data_list = NewModel.objects.all()  # NewModel 데이터의 모든 값들
        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})