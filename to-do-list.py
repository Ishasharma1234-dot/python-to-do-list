import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, bd=0, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_task = tk.Entry(root, width=54)
        self.entry_task.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_task_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        self.update_task_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_task_button.pack(side=tk.LEFT, padx=5)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(side=tk.LEFT, padx=5)

        self.load_tasks()

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = simpledialog.askstring("Update Task", "Update the selected task:")
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, new_task)
            else:
                messagebox.showwarning("Warning", "You must enter a new task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def load_tasks(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
