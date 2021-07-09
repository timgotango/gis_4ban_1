from django.db import models

# Create your models here.

class NewModel(models.Model): # models 패키지 안에 있는 Model을 상속받겠다
    text = models.CharField(max_length=255, null=False) # 캐릭터 필드를 통해 문자열을 받을 것이다(최대 255자, null 허용 안함)
