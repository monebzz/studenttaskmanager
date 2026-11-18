"""Tests for completing tasks (feature/completetask)."""

import unittest

from task_manager import TaskManager


class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager(storage_file=None)
        self.task = self.manager.add_task("CSC418 Assignment 4")

    def test_complete_task(self):
        """Marking a task complete sets completed to True."""
        completed = self.manager.complete_task(self.task["id"])
        self.assertTrue(completed["completed"])
        self.assertTrue(self.manager.list_tasks()[0]["completed"])

    def test_complete_unknown_task_raises(self):
        """Completing an unknown id raises ValueError."""
        with self.assertRaises(ValueError):
            self.manager.complete_task(99)


if __name__ == "__main__":
    unittest.main()
