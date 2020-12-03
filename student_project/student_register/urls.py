
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.student_form , name = 'student_insert'), #localhost/employee/list
    path('<int:id>/', views.student_form, name="student_update"),
    path('list/', views.student_list, name = 'studentlist'),
    path('delete/<int:id>/', views.student_delete, name = "studentDelete")
]
