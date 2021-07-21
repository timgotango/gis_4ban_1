from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel

@login_required(login_url=reverse_lazy('accountapp:login'))
# 장고에서 제공해주는 데코레이터(account/login으로 알아서 가준다 하지만 다르게 했다면, login_url로 redirect 가능!!)
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
    context_object_name = 'target_user'         # key
    template_name = 'accountapp/detail.html'    # 추후에 만들 detail.html

# class 안에 있는 함수이므로 '메소드'이다. 따라서 메소드용 함수를 만들지, 또는 decorator 자체를 변환할지 정해야. 우린 후자로.
@method_decorator(login_required, 'get')    # method_decorator로 decorator 메소드용으로도 사용 가능하게 해주는 데코레이터 적용. :get 메소드에 적용하겠다.
@method_decorator(login_required, 'post')    # pot 메소드에 적용하겠다.
class AccountUpdateView(UpdateView): # 내 정보 수정
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world') # 원래는 detail 페이지로 가면 좋지만, 상세 페이지마다 pk가 다르므로 이건 나중에 해보자
    template_name = 'accountapp/update.html'

@method_decorator(login_required, 'get')    # get 메소드에 적용하겠다.
@method_decorator(login_required, 'post')    # pot 메소드에 적용하겠다.
class AccountDeleteView(DeleteView): # 삭제이므로 form_class 없어도 된다.
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

