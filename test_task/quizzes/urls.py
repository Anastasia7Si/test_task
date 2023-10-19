from django.urls import include, path
from rest_framework.routers import DefaultRouter

from quizzes.views import QuizzeViewSet

app_name = 'quizzes'

router = DefaultRouter()
router.register('quizzes', QuizzeViewSet, basename='quizzes')

urlpatterns = [
    path('', include(router.urls)),
]
