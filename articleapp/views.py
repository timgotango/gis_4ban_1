from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('articleapp:list')   # 게시글의 디테일 페이지로 원래 가는게 좋지만 일단은
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user    # writer 변수에 request를 보내고 있는 user를 할당!
        return super().form_valid(form)