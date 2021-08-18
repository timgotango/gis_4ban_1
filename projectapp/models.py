from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # str 형으로 호출했을 때 어떻게 출력해줄 것이냐~를 정의해주기
    def __str__(self):
        return f'{self.name}'