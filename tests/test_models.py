# tests/test_models.py

from django.test import TestCase
from tests.models import Task   # ✅ FIXED IMPORT

class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(title="Learn Django")

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Learn Django")

    def test_task_str_method(self):
        self.assertEqual(str(self.task), "Learn Django")