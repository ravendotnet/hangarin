from django.core.management.base import BaseCommand
from faker import Faker
from webapp.models import Priority, Category, Task, Note, SubTask

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_task(10)
        self.create_note(10)
        self.create_subtask(10)

        self.stdout.write(
            self.style.SUCCESS('Fake data created successfully!')
        )

    def create_task(self, count):
        fake = Faker()

        priorities = list(Priority.objects.all())
        categories = list(Category.objects.all())

        for _ in range(count):
            Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=fake.date_this_month(),
                status=fake.random_element(
                    elements=[
                        "Pending",
                        "In Progress",
                        "Completed"
                    ]
                ),
                priority=fake.random_element(
                    elements=priorities
                ),
                category=fake.random_element(
                    elements=categories
                ),
            )

        self.stdout.write(self.style.SUCCESS
            ('Initial data for Tasks created successfully.')
        )

    def create_note(self, count):
        fake = Faker()

        tasks = list(Task.objects.all())

        for _ in range(count):
            Note.objects.create(
                task=fake.random_element(
                    elements=tasks
                ),
                content=fake.paragraph(nb_sentences=3),
            )
        self.stdout.write(self.style.SUCCESS
            ('Initial data for Notes created successfully.')
        )

    def create_subtask(self, count):
        fake = Faker()

        tasks = list(Task.objects.all())

        for _ in range(count):
            SubTask.objects.create(
                parent_task=fake.random_element(
                    elements=tasks
                ),
                title=fake.sentence(nb_words=5),
                status=fake.random_element(
                    elements=[
                        "Pending",
                        "In Progress",
                        "Completed"
                    ]
                ),
            )

        self.stdout.write(self.style.SUCCESS
            ('Initial data for SubTask created successfully.')
        )
    