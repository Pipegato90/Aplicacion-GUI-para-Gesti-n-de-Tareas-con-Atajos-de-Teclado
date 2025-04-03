import tkinter as tk
from tkinter import ttk, messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")

        # Configurar atajos de teclado
        self.root.bind('<Escape>', lambda e: self.root.destroy())
        self.root.bind('<Delete>', lambda e: self.delete_task())
        self.root.bind('d', lambda e: self.delete_task())
        self.root.bind('c', lambda e: self.complete_task())

        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Entrada de tarea
        ttk.Label(main_frame, text="Nueva Tarea:").pack(anchor=tk.W)
        self.task_entry = ttk.Entry(main_frame, width=50)
        self.task_entry.pack(fill=tk.X, pady=(0, 10))
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        self.task_entry.focus_set()

        # Botones
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, pady=(0, 10))

        self.add_button = ttk.Button(
            buttons_frame,
            text="Añadir (Enter)",
            command=self.add_task
        )
        self.add_button.pack(side=tk.LEFT, padx=(0, 5))

        self.complete_button = ttk.Button(
            buttons_frame,
            text="Completar (C)",
            command=self.complete_task
        )
        self.complete_button.pack(side=tk.LEFT, padx=(0, 5))

        self.delete_button = ttk.Button(
            buttons_frame,
            text="Eliminar (D/Delete)",
            command=self.delete_task
        )
        self.delete_button.pack(side=tk.LEFT)

        # Lista de tareas
        ttk.Label(main_frame, text="Lista de Tareas:").pack(anchor=tk.W)

        self.task_list = tk.Listbox(
            main_frame,
            height=15,
            selectmode=tk.SINGLE,
            activestyle='none'
        )
        self.task_list.pack(fill=tk.BOTH, expand=True)

        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.task_list)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_list.yview)

        # Tooltip para atajos
        ttk.Label(
            main_frame,
            text="Atajos: Enter=Añadir, C=Completar, D/Delete=Eliminar, Esc=Salir",
            font=('Arial', 8)
        ).pack(anchor=tk.W, pady=(5, 0))

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.task_list.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una tarea válida.")

    def complete_task(self):
        selected = self.task_list.curselection()
        if selected:
            index = selected[0]
            task_text = self.task_list.get(index)

            # Verificar si ya está marcada como completada
            if not task_text.startswith("✓ "):
                self.task_list.delete(index)
                self.task_list.insert(index, f"✓ {task_text}")
                self.task_list.itemconfig(index, {'fg': 'gray'})
            else:
                messagebox.showinfo("Info", "Esta tarea ya está completada.")
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")

    def delete_task(self):
        selected = self.task_list.curselection()
        if selected:
            self.task_list.delete(selected[0])
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()