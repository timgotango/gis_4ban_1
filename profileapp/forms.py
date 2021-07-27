from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:     # 이미지 같은 것들을 설명해주는 외부 정보들
        model = Profile
        fields = ['image', 'nickname', 'message']   # 이 3가지를 받겠다