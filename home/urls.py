
from django.urls import path,include
from . import views
urlpatterns = [
    
     path('', views.index),
   

     # path(, views.home,  name='home'),
     path('', views.index),

]

# from django.urls import path
# from . import views  # Import views from the same directory

# urlpatterns = [
#     # Other URL patterns
#     path('home/', views.home, name='home'),
# ]


