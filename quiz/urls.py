from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_view, name='login'),
    path('register/',views.register_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('quizzes/',views.quizzes, name='quizzes'),
    path('quizzes/category/<str:name>', views.category_view, name='category'),

]
