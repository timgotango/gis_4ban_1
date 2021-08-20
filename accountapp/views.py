from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel
from articleapp.models import Article


@login_required
# 장고에서 제공해주는 데코레이터(account/login으로 알아서 가준다. 하지만 다르게 했다면, login_url=''로 redirect 가능!!)
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
    template_name = 'accountapp/create.html' # 곧 만들 subscribe.html

    # def get_success_url(self):
    #     return reverse('accountapp:detail', self.object.pk) # accountapp이므로 바로 object.pk

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User # User 객체의 detail을 보는 것이기 때문에
    context_object_name = 'target_user'         # key
    template_name = 'accountapp/detail.html'    # 추후에 만들 detail.html
    paginate_by = 20
    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list, **kwargs)


has_ownership = [login_required, account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView): # 내 정보 수정
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    # success_url = reverse_lazy('accountapp:hello_world') # 원래는 detail 페이지로 가면 좋지만, 상세 페이지마다 pk가 다르므로 이건 나중에 해보자
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk}) # accountapp이므로 바로 object.pk

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView): # 삭제이므로 form_class 없어도 된다.
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

