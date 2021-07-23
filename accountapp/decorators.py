from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):        # 자기 계정이어야 한다
    def decorated(request, *args, **kwargs):    # 해당 target_user == request를 보내는 user와 동일한지!
        target_user = User.objects.get(pk=kwargs['pk'])             # User 클래스 - kwargs에서 pk를 찾기(get)
        if target_user == request.user:
            return func(request, *args, **kwargs)       # 동일하다면, 함수를 실행!
        else:
            return HttpResponseForbidden()                # 동일하지 않다면 forbidden
    return decorated        # 이건 객체 생성하면 안된다!!
