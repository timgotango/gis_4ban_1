from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'              # accountapp 이름을 적어주어 다른 파일에서 라우팅해줄 수 있는 것.

# name 인자를 기반으로 다른 파일에서 라우팅해줄 수 있는 것.
# path 인 hello_world/를 가져와야하므로 views.py에서 reverse 함수 사용!!
urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'), # create는 없는 것을 만드는 것
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), # 다만 detail은 주소<int:pk>를 넘겨받아야!
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'), # 정보 수정이므로 user 키값 받아야.
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'), # 회원 정보 삭제이므로 마찬가지로 pk 값 받아야
]