"""Tests for displaying tasks."""

import unittest

from task_manager import TaskManager


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager(storage_file=None)

    def test_display_empty(self):
        """An empty manager reports that there are no tasks yet."""
        self.assertIn("No tasks yet", self.manager.display_tasks())

    def test_display_shows_completed_marker(self):
        """A completed task is shown with the [x] marker."""
        task = self.manager.add_task("CSC418 Assignment 4")
        self.manager.complete_task(task["id"])
        # NOTE (first version): this expected "[done]" — wrong marker,
        # so this test failed until it was corrected to "[x]".
        self.assertIn("[done]", self.manager.display_tasks())


if __name__ == "__main__":
    unittest.main()
