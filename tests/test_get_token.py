import unittest
from unittest.mock import patch

from todoist_quick_capture.get_token import APP_NAME, SECRET_NAME, api_dialog_cli


class TestApiDialogCli(unittest.TestCase):
    @patch("todoist_quick_capture.get_token.input", return_value="your_token")
    @patch("todoist_quick_capture.get_token.keyring.set_password")
    @patch(
        "todoist_quick_capture.get_token.keyring.get_password",
        return_value="your_token",
    )
    def test_api_dialog_cli_success(
        self, mock_get_password, mock_set_password, mock_input
    ):
        # Act
        result = api_dialog_cli()

        # Assert
        mock_input.assert_called_once_with("Please enter your Todoist API token: ")
        mock_set_password.assert_called_once_with(APP_NAME, SECRET_NAME, "your_token")
        mock_get_password.assert_called_once_with(APP_NAME, SECRET_NAME)
        self.assertEqual(result, "your_token")
        print("API token stored securely.")

    @patch("todoist_quick_capture.get_token.input", return_value="your_token")
    @patch(
        "todoist_quick_capture.get_token.keyring.set_password",
        side_effect=Exception("Error storing API token"),
    )
    def test_api_dialog_cli_error(self, mock_set_password, mock_input):
        # Act and Assert
        with self.assertRaises(Exception):
            api_dialog_cli()

        mock_input.assert_called_once_with("Please enter your Todoist API token: ")
        mock_set_password.assert_called_once_with(APP_NAME, SECRET_NAME, "your_token")


# class TestApiDialogGui(unittest.TestCase):
#     @patch("todoist_quick_capture.get_token.keyring.set_password")
#     @patch("todoist_quick_capture.get_token.keyring.get_password")
#     @patch("todoist_quick_capture.get_token.tk.Toplevel")
#     @patch("todoist_quick_capture.get_token.tk.Label")
#     @patch("todoist_quick_capture.get_token.tk.Entry")
#     @patch("todoist_quick_capture.get_token.tk.Button")
#     def test_api_dialog_gui_success(
#         self,
#         mock_button,
#         mock_entry,
#         mock_label,
#         mock_toplevel,
#         mock_get_password,
#         mock_set_password,
#     ):
#         # Arrange
#         root = tk.Tk()
#         dialog = MagicMock()
#         mock_toplevel.return_value = dialog
#         api_entry = MagicMock()
#         mock_entry.return_value = api_entry
#         submit_button = MagicMock()
#         mock_button.return_value = submit_button

#         # Act
#         api_dialog_gui(root)

#         # Assert
#         mock_toplevel.assert_called_once_with(root)
#         dialog.attributes.assert_called_once_with("-type", "dialog")
#         dialog.title.assert_called_once_with("API Token Prompt")
#         dialog.geometry.assert_called_once_with("400x200")
#         mock_label.assert_called_once_with(dialog, text="Please enter your API token:")
#         mock_label.return_value.pack.assert_called_once()
#         mock_entry.assert_called_once_with(dialog, show="*")
#         mock_entry.return_value.pack.assert_called_once()
#         api_entry.focus_set.assert_called_once()

#     @patch("todoist_quick_capture.get_token.keyring.set_password")
#     @patch("todoist_quick_capture.get_token.keyring.get_password")
#     @patch("todoist_quick_capture.get_token.tk.Toplevel")
#     @patch("todoist_quick_capture.get_token.tk.Label")
#     @patch("todoist_quick_capture.get_token.tk.Entry")
#     @patch("todoist_quick_capture.get_token.tk.Button")
#     @patch("todoist_quick_capture.get_token.messagebox.showerror")
#     def test_api_dialog_gui_error(
#         self,
#         mock_showerror,
#         mock_button,
#         mock_entry,
#         mock_label,
#         mock_toplevel,
#         mock_get_password,
#         mock_set_password,
#     ):
#         # Arrange
#         root = tk.Tk()
#         dialog = MagicMock()
#         mock_toplevel.return_value = dialog
#         api_entry = MagicMock()
#         mock_entry.return_value = api_entry
#         submit_button = MagicMock()
#         mock_button.return_value = submit_button

#         # Act
#         api_dialog_gui(root)

#         # Assert
#         mock_toplevel.assert_called_once_with(root)
#         dialog.attributes.assert_called_once_with("-type", "dialog")
#         dialog.title.assert_called_once_with("API Token Prompt")
#         dialog.geometry.assert_called_once_with("400x200")
#         mock_label.assert_called_once_with(dialog, text="Please enter your API token:")
#         mock_label.return_value.pack.assert_called_once()
#         mock_entry.assert_called_once_with(dialog, show="*")
#         mock_entry.return_value.pack.assert_called_once()
#         api_entry.focus_set.assert_called_once()


if __name__ == "__main__":
    unittest.main()
