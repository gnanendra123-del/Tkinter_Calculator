import tkinter as tk
from tkinter import font as tkfont
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg="#000000")
        self.root.resizable(False, False)
        self.root.geometry("380x620")
        self.expression = ""
        self.setup_ui()
        self.bind_keys()
    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg="#000000")
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)
        display_frame = tk.Frame(main_frame, bg="#1c1c1c", bd=0)
        display_frame.pack(fill="x", pady=(0, 20))
        self.entry = tk.Entry(
            display_frame,
            font=("Segoe UI", 36, "bold"),
            bg="#1c1c1c",
            fg="#ffffff",
            bd=0,
            justify="right",
            insertbackground="#ffffff"
        )
        self.entry.pack(fill="x", padx=20, pady=25)
        buttons_frame = tk.Frame(main_frame, bg="#000000")
        buttons_frame.pack(fill="both", expand=True)
        buttons = [
            ('C', 0, 0, 2, '#505050', '#606060'),
            ('⌫', 0, 2, 2, '#505050', '#606060'),
            ('7', 1, 0, 1, '#333333', '#3d3d3d'),
            ('8', 1, 1, 1, '#333333', '#3d3d3d'),
            ('9', 1, 2, 1, '#333333', '#3d3d3d'),
            ('÷', 1, 3, 1, '#ff9f0a', '#ffb340'),
            ('4', 2, 0, 1, '#333333', '#3d3d3d'),
            ('5', 2, 1, 1, '#333333', '#3d3d3d'),
            ('6', 2, 2, 1, '#333333', '#3d3d3d'),
            ('×', 2, 3, 1, '#ff9f0a', '#ffb340'),
            ('1', 3, 0, 1, '#333333', '#3d3d3d'),
            ('2', 3, 1, 1, '#333333', '#3d3d3d'),
            ('3', 3, 2, 1, '#333333', '#3d3d3d'),
            ('−', 3, 3, 1, '#ff9f0a', '#ffb340'),
            ('0', 4, 0, 2, '#333333', '#3d3d3d'),
            ('.', 4, 2, 1, '#333333', '#3d3d3d'),
            ('+', 4, 3, 1, '#ff9f0a', '#ffb340'),
            ('=', 5, 0, 4, '#34c759', '#40d965'),
        ]
        for text, row, col, colspan, bg, hover in buttons:
            cmd = self.get_command(text)
            btn = self.create_button(buttons_frame, text, cmd, bg, hover)
            btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")
        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1, minsize=70)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1, minsize=70)
    
    def create_button(self, parent, text, command, bg_color, hover_color):
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 22, "normal"),
            bg=bg_color,
            fg="white",
            bd=0,
            activebackground=hover_color,
            activeforeground="white",
            relief="flat",
            cursor="hand2"
        )
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))
        return btn
    def get_command(self, text):
        if text == 'C':
            return self.clear
        elif text == '⌫':
            return self.backspace
        elif text == '=':
            return self.calculate
        elif text == '÷':
            return lambda: self.press('/')
        elif text == '×':
            return lambda: self.press('*')
        elif text == '−':
            return lambda: self.press('-')
        else:
            return lambda: self.press(text)
    def press(self, value):
        self.entry.insert(tk.END, value)
    def clear(self):
        self.entry.delete(0, tk.END)
    def backspace(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current[:-1])
    def calculate(self):
        try:
            result = str(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")
    def bind_keys(self):
        self.root.bind("<Key>", self.key_press)
    def key_press(self, event):
        if event.char in "0123456789+-*/.":
            self.press(event.char)
        elif event.keysym == "Return":
            self.calculate()
        elif event.keysym == "BackSpace":
            self.backspace()
        elif event.char.lower() == "c":
            self.clear()
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
