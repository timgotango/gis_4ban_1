
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(CreateView):
    model = Profile     # models.py에서 Profile 모델 만들어준 것
    form_class = ProfileCreationForm    # forms.py에서 class(image, nickname, message) 만들어준 것
    template_name = 'profileapp/create.html'    # 추후에 만들 html 파일

    def form_valid(self, form):     # 검증이 완료되면 form_valid 함수가 적용된다. 커스터마이징 하려고 오버라이딩
        form.instance.user = self.request.user  # user를 할당한 것!(forms.py에는 user가 필드에 없으므로)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile' # html에서 어떻게 부를것인지
    template_name = 'profileapp/update.html'
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk}) # target_profile에 연결되어 있는 유저의 pk를 가져온 것
