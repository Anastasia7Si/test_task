from rest_framework.viewsets import ModelViewSet

from quizzes.models import Quizzes
from quizzes.serializers import QuizzesPostSerializer


class QuizzeViewSet(ModelViewSet):
    queryset = Quizzes.objects.all()
    serializer_class = QuizzesPostSerializer
