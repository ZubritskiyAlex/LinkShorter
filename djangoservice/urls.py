from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views
import users.views

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('home/', views.homepage, name='home'),
    path('create-link/', views.create_link, name='create-link'),
    path('login/', users.views.login_page, name='login'),
    path('logout/', users.views.logout_user, name='logout'),
    path('links/', views.all_links, name='links'),
    path('mylinks/', views.get_my_links, name='mylinks'),
    path('signup/', users.views.signup, name='signup'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
