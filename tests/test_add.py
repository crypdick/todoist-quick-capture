import unittest
from unittest.mock import patch

from todoist_quick_capture.add import add_task


class TestAddTask(unittest.TestCase):
    @patch("todoist_quick_capture.add.TodoistAPI")
    def test_add_task_success(self, mock_todoist_api):
        # Arrange
        text = "Buy groceries"
        token = "your_token"
        task_id = 12345
        mock_task = mock_todoist_api.return_value.quick_add_task.return_value
        mock_task.data = {"task_id": task_id}

        # Act
        add_task(text, token)

        mock_todoist_api.assert_called_once_with(token)
        mock_todoist_api.return_value.quick_add_task.assert_called_once_with(text=text)

    @patch("todoist_quick_capture.add.TodoistAPI")
    def test_add_task_error(self, mock_todoist_api):
        # Arrange
        text = "Invalid task"
        token = "your_token"
        mock_todoist_api.return_value.quick_add_task.side_effect = Exception(
            "Invalid task"
        )

        # Act and Assert
        with self.assertRaises(Exception):
            add_task(text, token)
        mock_todoist_api.assert_called_once_with(token)
        mock_todoist_api.return_value.quick_add_task.assert_called_once_with(text=text)

    def test_add_task_empty_text(self):
        # Arrange
        text = ""
        token = "your_token"

        # Act and Assert
        with self.assertRaises(AssertionError):
            add_task(text, token)


if __name__ == "__main__":
    unittest.main()
