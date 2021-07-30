from django.urls import path
from django.views.generic import TemplateView
 
app_name='articleapp'   # articleapp의 templates에 접근하기 위해 설정해줌

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
]