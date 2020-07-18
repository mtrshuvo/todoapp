
from django.urls import path,include
from mytask import views


app_name= 'mytask'

urlpatterns = [
    path('',views.index,name='task'),
    path('update/<str:pk>/',views.updateTask,name='update'),
    path('delete/<str:pk>/',views.deleteTask,name='delete')

]
