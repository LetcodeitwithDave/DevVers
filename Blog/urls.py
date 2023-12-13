from django.urls import path
from  . import views
from core import views as api
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", views.about, name="blog-about"),
    path('login/', views.loginpage, name="blog-login"),
    path('register/', views.register, name="blog-register"),
    path('logout/', views.logoutpage, name="blog-logout"),
    path('post/', views.post, name="blog-post"),
    path('home/', views.home, name="blog-home"),
    path('post/<int:post_id>', views.readpost, name="blog-readpost"),
    path('edit/<int:edit_id>', views.edit, name="blog-edit"),
    path('delete/<int:delete_id>', views.delete, name = 'blog-delete'),
    path('delete_confirm/<int:id>', views.delete_confirmation, name = 'blog-delete_confirm'),

    path('blog/search/', views.search, name = 'blog-search'),
    path('blog/api/', api.post_list, name = 'blog-api'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
