from django.contrib import admin
from django.urls import path

from COLLEGE_APP import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('signinpage',views.signinpage,name='signinpage'),
    path('signin',views.signin,name='signin'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('teacher_home',views.teacher_home,name='teacher_home'),
    path('course',views.course,name='course'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('student',views.student,name='student'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('student_data',views.student_data,name='student_data'),
    path('user_data',views.user_data,name='user_data'),
    path('userdelete/<int:pk>',views.userdelete,name='userdelete'),
    path('studentdelete/<int:pk>',views.studentdelete,name='studentdelete'),
    path('user_view/<int:pk>',views.user_view,name='user_view'),
    path('std_editpage/<int:pk>',views.std_editpage,name='std_editpage'),
    path('std_edit/<int:pk>',views.std_edit,name='std_edit'),
]