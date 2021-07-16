from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from accountapp.models import NewModel

def hello_world(request):
    if request.method == "POST": # request 안에 method라는 데이터가 POST 방식이라면,

        temp = request.POST.get('input_text') # request 안에 있는 POST 데이터 중, input_text 라는 이름을 가져와~~

        new_model = NewModel() # models.py의 NewModel 클래스 객체 생성
        new_model.text = temp # NewModel 안 text에 input한 것을 넣는 것.
        new_model.save() # 저장까지 해줘야!

        # 보여지는 작업을 GET 으로 넘겨주기
        # reverse 함수 : urls.py에서 name 인자를 가져온 후 path로 역으로 가져온다
        return HttpResponseRedirect(reverse('accountapp:hello_world'))  # Redirect

    else: # GET 방식이라면,
        data_list = NewModel.objects.all()  # NewModel 데이터의 모든 값들
        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})

class AccountCreateView(CreateView): # 장고의 뷰의 제너릭에서 CreateView import
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # 함수가 아니라 클래스에서 사용하기 때문에 reverse_lazy 사용
    template_name = 'accountapp/create.html' # 곧 만들 create.html

class AccountDetailView(DetailView):
    model = User # User 객체의 detail을 보는 것이기 때문에
    context_object_name = 'target_user'         # context_object_name
    template_name = 'accountapp/detail.html'    # 추후에 만들 detail.html