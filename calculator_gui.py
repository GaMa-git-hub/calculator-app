import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get().replace('^', '**'))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator GUI")

entry = tk.Entry(root, width=30, borderwidth=3, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('^', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('=', 5, 1)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=20, height=2, command=calculate).grid(row=row, column=col, columnspan=3)
    elif text == 'C':
        tk.Button(root, text=text, width=5, height=2, command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click(t)).grid(row=row, column=col)

root.mainloop()
