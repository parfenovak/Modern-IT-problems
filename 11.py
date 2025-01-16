import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Ошибка", "Деление на ноль невозможно")
                return
            result = num1 / num2
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

def show_selection():
    selected = []
    if var1.get():
        selected.append("Первый")
    if var2.get():
        selected.append("Второй")
    if var3.get():
        selected.append("Третий")
    if selected:
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selected)}")
    else:
        messagebox.showinfo("Выбор", "Вы ничего не выбрали")

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

root = tk.Tk()
root.title("Парфенова Екатерина Евгеньевна")  

notebook = ttk.Notebook(root)
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)
notebook.add(tab1, text="Калькулятор")
notebook.add(tab2, text="Чекбоксы")
notebook.add(tab3, text="Текст")
notebook.pack(expand=True, fill="both")

entry1 = tk.Entry(tab1)
entry1.pack(pady=5)
entry2 = tk.Entry(tab1)
entry2.pack(pady=5)

operation_var = tk.StringVar(value="+")
operation_menu = tk.OptionMenu(tab1, operation_var, "+", "-", "*", "/")
operation_menu.pack(pady=5)

calculate_button = tk.Button(tab1, text="Вычислить", command=calculate)
calculate_button.pack(pady=5)

result_label = tk.Label(tab1, text="Результат: ")
result_label.pack(pady=5)

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

checkbox1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
checkbox1.pack(pady=5)
checkbox2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
checkbox2.pack(pady=5)
checkbox3 = tk.Checkbutton(tab2, text="Третий", variable=var3)
checkbox3.pack(pady=5)

show_button = tk.Button(tab2, text="Показать выбор", command=show_selection)
show_button.pack(pady=5)

text_area = tk.Text(tab3)
text_area.pack(expand=True, fill="both", padx=5, pady=5)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть файл", command=load_file)
menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()