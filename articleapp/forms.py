from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    # class : editable을 가지고 있는 속성의 textarea를 적용!!
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'min-height: 10rem;'
                                                                    'text-align: left;'}))
    class Meta:
        model = Article
        fields = ['project', 'title', 'image', 'content']