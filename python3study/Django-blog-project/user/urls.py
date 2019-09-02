from django.urls import path, re_path
from .views import reg

urlpatterns = [
    re_path('reg', reg),
]
