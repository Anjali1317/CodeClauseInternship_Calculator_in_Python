import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.entry = tk.Entry(root, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)
        
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=20, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col)

    def button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
        elif text == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
