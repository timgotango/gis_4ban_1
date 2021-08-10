from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def get_success_url(self):  # 그냥 success_url 인자로만은 하나의 페이지로밖에 못가기 때문!
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})