from django.urls import path
from .views import *

urlpatterns=[
    path('',view=callques,name="Quizpage"),
    path('result',view=get_ans)
]