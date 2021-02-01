from django.urls import path
from . import views

app_name="lenders"

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name = 'upload-lender'),
    path('update/<int:lender_id>', views.update_lender),
    path('delete/<int:lender_id>', views.delete_lender),
    path('register/' , views.register , name="register"),
    path('logout/' , views.logout_request , name="logout"),
    path('login/' , views.login_request , name="login"),
    path('calculate/' , views.calculate , name="calculate"),
]