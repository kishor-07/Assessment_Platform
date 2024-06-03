from django.urls import path,include
from . import views


urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('adlog/',views.adlog_view,name='adlog'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('quiz/',views.quiz_view,name='quiz'),
    path('course',views.course_view,name='course'),
    path('short',views.short_view,name='short'),
    path('pro',views.program_view,name='pro'),
    path('runcode',views.runcode,name='runcode')
]