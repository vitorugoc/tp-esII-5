import unittest
from tasks import TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task('Test task')
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].description, 'Test task')
        self.assertFalse(tasks[0].completed)

    def test_list_tasks(self):
        self.manager.add_task('Task 1')
        self.manager.add_task('Task 2')
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)

    def test_complete_task(self):
        self.manager.add_task('Test task')
        tasks = self.manager.list_tasks()
        self.manager.complete_task(1)
        self.assertTrue(tasks[0].completed)

    def test_complete_task_invalid_id(self):
        self.manager.add_task('Test task')
        with self.assertRaises(ValueError):
            self.manager.complete_task(99)

    def test_clear_tasks(self):
        self.manager.add_task('Test task')
        self.manager.clear_tasks()
        self.assertEqual(len(self.manager.list_tasks()), 0)

if __name__ == '__main__':
    unittest.main()
