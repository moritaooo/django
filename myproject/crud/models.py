from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name + str(self.price)
    

#モデルを編集した後はマイグレーションをする。（ビューがモデルを使ってDBに読み書きしに行く時、モデルの内容とDBの内容が食い違い、エラーが起こる）
