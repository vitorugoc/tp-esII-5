class Task:
    """Representa uma tarefa individual."""
    _id_counter = 1
    
    def __init__(self, description):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.description = description
        self.completed = False

    def complete(self):
        """Marca a tarefa como concluída."""
        self.completed = True

    def __repr__(self):
        return f'Task(id={self.id}, description="{self.description}", completed={self.completed})'


class TaskManager:
    """Gerencia uma lista de tarefas."""
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        """Adiciona uma nova tarefa."""
        task = Task(description)
        self.tasks.append(task)

    def list_tasks(self):
        """Retorna todas as tarefas."""
        return self.tasks

    def complete_task(self, task_id):
        """Marca uma tarefa como concluída pelo ID."""
        for task in self.tasks:
            if task.id == task_id:
                task.complete()
                return
        raise ValueError(f"Tarefa com id {task_id} não encontrada.")

    def clear_tasks(self):
        """Limpa todas as tarefas (usado para testes)."""
        self.tasks = []
        Task._id_counter = 1

if __name__ == '__main__':
    manager = TaskManager()
    manager.add_task("Teste 1")
    manager.add_task("Teste 2")
    print("Todas as Tarefas:", manager.list_tasks())
    manager.complete_task(1)
    print("Tarefas após conclusão:", manager.list_tasks())