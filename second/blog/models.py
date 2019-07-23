# 백엔드 에서 가장 중요한게 models.py -> 데이터관리

from django.db import models

class Blog(models.Model):
    #어떤 변수에 어떤 타입의 데이터를 받아줄지 작성
    title = models.CharField(max_length=200)    # title 변수에 짧은문자열데이터(charfield)저장. 최대길이 200
    pub_date =models.DateTimeField('data published')  # publish_date ''로 처리해주겠다
    body = models.TextField()  # body변수에 긴 문자열 데이터(textField)

    def __str__(self):  # 블로그 제목을 title로 하고싶을때.  얘가없으면 blog object(1) 이런식으로 나온다.
        return self.title

    def summary(self):  # body  100글자 상한선
        return self.body[:100]