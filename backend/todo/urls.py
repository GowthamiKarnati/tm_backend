from django.urls import path, include   
from todo import views                            # add this
from rest_framework import routers                    # add this
               # add this

router = routers.DefaultRouter()                      # add this
router.register(r'tasks', views.TodoView, 'task')     # add this

# from django.urls import path  - DELETE THIS

urlpatterns = [
    
    path('', include(router.urls))                # add this
]
