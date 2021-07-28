from django.urls import path

from profileapp.views import ProfileCreateView

app_name = 'profileapp'     # 이렇게 app_name 설정해주어야 나중에 'profileapp:create' 와 같은 방식으로 정해줄 수 있음!!

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),

]