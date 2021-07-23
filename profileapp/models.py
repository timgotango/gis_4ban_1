from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # OneToOneField : User DB와 연결해주는 필드 / on_delete : User 객체가 삭제가 되었을 때, 행동을 정할 수 있다. (CASCADE : 프로필도 삭제해라~)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # 사용 시, user.profile 로 접근 가능하게끔
    # 이미지를 받았을 때 저장하는 경로 (MEDIA_ROOT 안에서 profile 이라는 별도의 폴더를 만들고 여기다 저장해주겠다)
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)  # null : 안적어도 되는 것.
    message = models.CharField(max_length=200, null=True)

    # 모델 변화시키면 무조건 migrate 해야!!
