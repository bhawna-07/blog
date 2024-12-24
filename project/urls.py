
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('createblog/',views.createblog,name='create'),
    path('table/',views.blog_table,name='table'),
    path('detail/<int:id>/', views.blog_detail, name='blog_detail'),  
    path('logut/',views.user_logout,name='logout') ,
    path('update/<int:id>/',views.blog_update,name='update'),
    path('delete/<int:id>/',views.delete_data,name='delete'),
    
    ]
