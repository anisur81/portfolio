# from django.db import models

# Create your models here.
# your_app/tests/test_models.py

from django.test import TestCase
from tests.models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(title="Learn Django")

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Learn Django")

    def test_task_str_method(self):
        self.assertEqual(str(self.task), "Learn Django")