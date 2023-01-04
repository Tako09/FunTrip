from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ['user_name', 'birthday', 'email_address',] # 順番を固定する
    list_display = ('user_name', 'birthday', 'email_address', 'get_age', 'register_date') # チェンジリストに表示するフィールドを決める
    # list_filter = ['pub_date'] # フィルター機能を追加
    search_fields = ['user_name'] # 検索昨日を追加　Likeクエリで曖昧検索をしている
    list_per_page = 10 # ページ分割機能
    
admin.site.register(User, UserAdmin)