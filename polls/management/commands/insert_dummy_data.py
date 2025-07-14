from django.core.management.base import BaseCommand
from polls.models import Question, Choice
import random

class Command(BaseCommand):
    help = "Insert dummy questions and choices"

    def handle(self, *args, **kwargs):
        # Clear existing data
        Question.objects.all().delete()

        for i in range(5):  # 5 questions
            q = Question.objects.create(question_text=f"Sample Question {i + 1}")
            self.stdout.write(self.style.SUCCESS(f"Created Question: {q.question_text}"))

            for j in range(4):  # 4 choices per question
                c = Choice.objects.create(
                    question=q,
                    choice_text=f"Choice {j + 1} for Question {i + 1}",
                    votes=random.randint(0, 50)
                )
                self.stdout.write(f"  ↳ Added Choice: {c.choice_text} with {c.votes} votes")

        self.stdout.write(self.style.SUCCESS("✅ Dummy questions and choices inserted!"))
