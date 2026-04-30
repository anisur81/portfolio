from django.tests import TestCase
from tests.models import Task   # ✅ FIXED

class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(title="Learn Django")

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Learn Django")

    def test_task_str_method(self):
        self.assertEqual(str(self.task), "Learn Django")