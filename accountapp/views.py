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


class AccountCreateView(CreateView): # 장고의 뷰의 제너릭에서 CreateView import
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list') # 함수가 아니라 클래스에서 사용하기 때문에 reverse_lazy 사용
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
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk}) # accountapp이므로 바로 object.pk

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView): # 삭제이므로 form_class 없어도 된다.
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/delete.html'

