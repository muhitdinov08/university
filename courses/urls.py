from django.urls import path

from courses.views import home_page, teacher_detail, speciality_detail, speciality_create, teacher_create, teacher_list, \
    specialty_list, subject_list

app_name = "courses"
urlpatterns = [
    path('', home_page, name='home-page'),
    path('specility/create', speciality_create, name='speciality-create'),
    path('teacher/create', teacher_create, name='teacher-create'),
    path('teacher/<id>', teacher_detail, name='teacher-detail'),
    path('specility/<id>', speciality_detail, name='speciality-detail'),
    path('teacher_list/', teacher_list, name='teacher-list'),
    path('specility_list/', specialty_list, name='speciality-list'),
    path('subject_list/', subject_list, name='subject-list'),

]
