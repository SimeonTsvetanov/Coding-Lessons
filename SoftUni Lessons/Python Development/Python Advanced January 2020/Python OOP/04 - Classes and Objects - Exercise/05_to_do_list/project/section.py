from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        present_task = [task for task in self.tasks if task == new_task]  # TODO Check by name if problem
        if present_task:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        found_task = [t for t in self.tasks if t.name == task_name]
        if found_task:
            found_task[0].completed = True
            return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        len_tasks = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                len_tasks += 1
        return f"Cleared {len_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for t in self.tasks:
            result += f"{t.details()}\n"
        return result[:-1]
