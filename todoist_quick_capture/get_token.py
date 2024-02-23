import tkinter as tk
from tkinter import messagebox
from typing import Any, Optional

import keyring

APP_NAME = "todoist_quick_capture"
SECRET_NAME = "todoist_api_token"


def get_api_token(root: Optional[Any] = None) -> str:
    existing_token = keyring.get_password(APP_NAME, SECRET_NAME)
    if existing_token:
        return existing_token
    else:
        print("No existing token found.")
        if root:
            token = api_dialog_gui(root)
        else:
            token = api_dialog_cli()

        return token


def api_dialog_gui(root):
    print("Opening API token prompt...")

    def store_api_token():
        api_token = api_entry.get()
        if api_token:
            keyring.set_password(APP_NAME, SECRET_NAME, api_token)
            print("API token stored securely.")
            dialog.destroy()
        else:
            messagebox.showerror("Error", "Please enter an API token.")

    # Create Tkinter dialog window
    dialog = tk.Toplevel(root)
    dialog.attributes(
        "-type", "dialog"
    )  # Make the window a dialog so that i3 will float it
    dialog.title("API Token Prompt")

    dialog.geometry("400x200")  # Set the initial size of the window

    # Create label
    label = tk.Label(dialog, text="Please enter your API token:")
    label.pack()

    # Create entry widget
    api_entry = tk.Entry(dialog, show="*")
    api_entry.pack()
    api_entry.focus_set()
    api_entry.bind("<Return>", lambda event: store_api_token())

    # Create button to submit token
    submit_button = tk.Button(dialog, text="Submit", command=store_api_token)
    submit_button.pack()

    # Wait for the dialog window to be destroyed
    dialog.wait_window()

    # Once the dialog window is destroyed, return the API token
    return keyring.get_password(APP_NAME, SECRET_NAME)


def api_dialog_cli():
    api_token = input("Please enter your Todoist API token: ")
    keyring.set_password(APP_NAME, SECRET_NAME, api_token)
    print("API token stored securely.")
    return keyring.get_password(APP_NAME, SECRET_NAME)
