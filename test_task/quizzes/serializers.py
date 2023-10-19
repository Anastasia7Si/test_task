from rest_framework import serializers
import requests
from quizzes.models import Quizzes


class QuizzesGetSerializer(serializers.ModelSerializer):
    """Сериализатор представления вопроса."""
    question_text = Quizzes.objects.order_by('-id')[1:1]

    class Meta:
        model = Quizzes
        fields = ('question_text',)


class QuizzesPostSerializer(serializers.ModelSerializer):
    """Сериализатор записи викторины."""
    class Meta:
        model = Quizzes
        fields = ('count',)
        read_only_fields = ('question_id', 'question_text',
                            'answer_text', 'date')

    def create(self, validated_data):
        count = validated_data.pop('count')
        ENDPOINT = f'https://jservice.io/api/random?count={count}'
        response = requests.get(ENDPOINT).json()
        for n in range(count):
            question = response[n]['question']
            answer = response[n]['answer']
            id = response[n]['id']
            created_at = response[n]['created_at']
            quizzes = Quizzes.objects.create(
               question_id=id, question_text=question,
               answer_text=answer, date=created_at)
        return quizzes

    def to_representation(self, data):
        return QuizzesGetSerializer(data).data
