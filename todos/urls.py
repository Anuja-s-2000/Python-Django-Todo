from django.urls import path
from todos import views
app_name = "todos"
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:uid>/', views.index, name="index"),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    path('<int:uid>/<int:todo_id>/delete', views.delete, name='delete'),
    path('<int:uid>/<int:todo_id>/update', views.update, name='update'),
    path('<int:uid>/add/', views.add, name='add'),
    path('<int:uid>/search/', views.search, name='search')
]