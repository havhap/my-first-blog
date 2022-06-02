from django.contrib import admin
from .models import Post

admin.site.register(Post)
#post 모델 불러오기
#이렇게 하면 글생성 모델도 불러올 수 있는지 아니면 그거랑은 다른 유형의 모델인지?