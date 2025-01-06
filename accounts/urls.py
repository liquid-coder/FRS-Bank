from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile' ),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('admin/approve_loan/<int:loan_id>/', views.approve_loan, name='approve_loan'),
    path('admin/disapprove_loan/<int:loan_id>/', views.disapprove_loan, name='disapprove_loan'),
]