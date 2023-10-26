import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, Root):
        self.Root = Root
        self.Root.title("To-Do List App")
        self.Tasks = []
        
        # Task input field
        self.Task_Entry = tk.Entry(Root, width=40)
        self.Task_Entry.pack(pady=10)
        
        # Add task button
        Add_Button = tk.Button(Root, text="Add Task", command=self.add_task)
        Add_Button.pack(pady=10)
        
        # Task list
        self.Task_Listbox = tk.Listbox(Root, width=40)
        self.Task_Listbox.pack(pady=10)
        
        # Remove task button
        Remove_Button = tk.Button(Root, text="Remove Task", command=self.Remove_Task)
        Remove_Button.pack(pady=10)
        
    def add_task(self):
        Task = self.Task_Entry.get()
        if Task:
            self.Tasks.append(Task)
            self.Task_Listbox.insert(tk.END, Task)
            self.Task_Entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    
    def Remove_Task(self):
        Selected_Task_Index = self.Task_Listbox.curselection()
        if Selected_Task_Index:
            Task_Index = Selected_Task_Index[0]
            del self.Tasks[Task_Index]
            self.Task_Listbox.delete(Task_Index)
        else:
            messagebox.showwarning("Warning", "Select a task to remove!")

if __name__ == "__main__":
    Root = tk.Tk()
    App = ToDoListApp(Root)
    Root.mainloop()