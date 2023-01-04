import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20)
    birthday = models.DateField('誕生日')
    email_address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user_name # Questionオブジェクトの戻り値をquestion_textにしている
    
    @admin.display(
        boolean=None,
        ordering='birthday',
        description='年齢'   
    )
    def get_age(self):
        """誕生日から年齢を取得する"""
        today = datetime.date.today()
        return (int(today.strftime("%Y%m%d")) - int(self.birthday.strftime("%Y%m%d"))) // 10000
    
    @admin.display(
        boolean=None,
        description='登録日'   
    )
    def register_date(self):
        """誕生日から年齢を取得する"""
        return datetime.date.today()
