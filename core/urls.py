from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add',views.add_student,name='add'),
    path('list',views.student_list,name='list'),
    path('delete/<int:id>/',views.student_delet,name='delete')
]
