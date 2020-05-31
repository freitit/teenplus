from django.urls import path
from django.contrib.auth import views as authviews


from . import views
from .forms import AuthenForm

urlpatterns = [
    path('', views.index, name='index'),
    path('show',views.showPost),
    path('show/<int:user_id>',views.showPost),
    path('addPost', views.addPost, name='addpost'),
    path('editPost/<int:id>', views.editPost),
    path('updatePost/<int:id>', views.updatePost),  
    path('removePost/<int:id>', views.removePost),
    path('login', authviews.LoginView.as_view(form_class=AuthenForm), name='login'),
    path('logout', authviews.LogoutView.as_view(), name='logout'),
    
    
]

# path('ajax/increase', views.increaseActionNumber, name='increaseActionNumber'),
# path('ajax', views.getActionNumber, name='getActionNumber')