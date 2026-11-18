"""Tests for deleting tasks (feature/deletetask)."""

import unittest

from task_manager import TaskManager


class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager(storage_file=None)
        self.first = self.manager.add_task("CSC418 Assignment 4")
        self.second = self.manager.add_task("Revise for viva")

    def test_delete_task(self):
        """Deleting a task removes only that task."""
        deleted = self.manager.delete_task(self.first["id"])
        self.assertEqual(deleted["title"], "CSC418 Assignment 4")
        remaining = self.manager.list_tasks()
        self.assertEqual(len(remaining), 1)
        self.assertEqual(remaining[0]["title"], "Revise for viva")

    def test_delete_unknown_task_raises(self):
        """Deleting an unknown id raises ValueError and deletes nothing."""
        with self.assertRaises(ValueError):
            self.manager.delete_task(99)
        self.assertEqual(len(self.manager.list_tasks()), 2)


if __name__ == "__main__":
    unittest.main()
