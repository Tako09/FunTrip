from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    # name 引数を定義したので、テンプレートタグの {%url%} を使用して、
    # URL 設定で定義されている特定の URL パスへの依存をなくすことができます:
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:pk>/votes/', views.votes, name='votes'),
]