from django.urls import  path
from . import views

urlpatterns = [
    path('', views.member_list, name='User list'),
    path('Add/', views.add_member, name='Add user'),
    path('Edit/<int:id>/', views.edit_member, name='Edit user'),
    path('Delete/<int:eid>/', views.delete_member, name='Delete user'),
    path('View/<eid>', views.view_member, name='View user'),
    path('cont', views.contribution_detail, name='Contribution detail'),
]