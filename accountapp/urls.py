from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'              # accountapp 이름을 적어주어 다른 파일에서 라우팅해줄 수 있는 것.

# name 인자를 기반으로 다른 파일에서 라우팅해줄 수 있는 것.
# path 인 hello_world/를 가져와야하므로 views.py에서 reverse 함수 사용!!
urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'),
]