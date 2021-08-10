from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment  # 이 모델을 사용할 것이다
        fields = ['content']    # 무엇을 입력받을 것인지