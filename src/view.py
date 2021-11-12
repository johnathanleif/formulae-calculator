import tkinter as tk

FORMULA_ENTRY_LABEL = "Input Formula:"

def open_window():
    window = tk.Tk()
    create_formula_input_section()
    window.mainloop()

def create_formula_input_section():
    label = tk.Label(text = FORMULA_ENTRY_LABEL)
    entry = tk.Entry(bg = "white", fg = "black")
    label.pack()
    entry.pack()

