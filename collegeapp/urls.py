from django.urls import path
from . import views
app_name ="collegeapp"
urlpatterns = [
    path('', views.applied_list, name="applied_list"),
    path('apply/', views.apply_link, name='apply_link'),
    path('eligible/', views.eligible, name='eligible')

]
