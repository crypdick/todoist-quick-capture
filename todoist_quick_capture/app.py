import subprocess
import tkinter as tk
from tkinter import messagebox

from add import add_task


def call_add_task():
    task = task_entry.get()
    # due_date = due_entry.get() if due_entry.get() else None
    # priority = priority_entry.get() if priority_entry.get() else None
    if task:
        try:
            # task = add_task(task=task, due=due_date, priority=priority)
            task = add_task(task)
            print(f"Task added successfully! {task}")
            root.destroy()  # Close the window
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to add task: {e}")


def focus_next_entry(event, entry):
    """Makes enter key move focus to the next entry widget."""
    entry.tk_focusNext().focus()
    return "break"  # Prevent default behavior of the enter key


root = tk.Tk()
root.attributes("-type", "dialog")  # Make the window a dialog so that i3 will float it
root.title("Add Task to Todoist")

root.geometry("400x200")  # Set the initial size of the window

task_label = tk.Label(root, text="Enter task:")
task_label.pack()

task_entry = tk.Entry(root, width=50)
task_entry.pack()
task_entry.focus_set()
task_entry.bind("<Return>", lambda event: call_add_task())


add_button = tk.Button(root, text="Add Task", command=call_add_task)
add_button.pack()

root.bind("<Return>", lambda event: call_add_task())

root.mainloop()
