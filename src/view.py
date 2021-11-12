import tkinter as tk
from tkinter import ttk


WINDOW_TITLE = "Formulae Calculator"
FORMULA_ENTRY_LABEL = "Input Formula:"
PARSE_BUTTON_LABEL = "Parse" 
CALC_BUTTON_LABEL = "Calculate"
RESULT_LABEL = "Result = "

ENTRY_BG = "white"
ENTRY_FG = "black"

VARIABLE_ENTRY_COLUMNS = 2

class TkView:

    def __init__(self, parse_observer, calculate_observer):
        self.parse_observer = parse_observer
        self.calculate_observer = calculate_observer
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)



    def open_window(self):
        self.create_formula_input()
        self.root.mainloop()


    def create_formula_input(self):
        frame = tk.Frame(self.root)
        frame.pack()

        entry_label = tk.Label(frame, text = FORMULA_ENTRY_LABEL)
        entry = tk.Entry(frame, bg = ENTRY_BG, fg = ENTRY_FG)
        parse_button = tk.Button(frame, text = PARSE_BUTTON_LABEL, command = lambda: self.parse(entry.get()))

        entry_label.pack(side = tk.LEFT)
        entry.pack(side = tk.LEFT)
        parse_button.pack(side = tk.RIGHT)

    def parse(self, input_formula_string):
        self.parse_observer.notify(input_formula_string)


    def create_separator(self):
        separator = ttk.Separator(self.root)
        separator.pack(fill = 'x')
    

    def create_variable_input(self, variables):
        self.create_separator()

        variable_frame = tk.Frame(self.root)
        variable_frame.pack()
    
        variables_grid_frame = tk.Frame(variable_frame)
        variables_grid_frame.pack()

        var_entries = {}
        row = 0
        col = 0
        for var in variables:
            frame = tk.Frame(variables_grid_frame)
            frame.grid(row = row, column = col)
            
            col += 1
            if col == VARIABLE_ENTRY_COLUMNS:
                col = 0
                row += 1

            entry_label = tk.Label(frame, text = var)
            entry = tk.Entry(frame, bg = ENTRY_BG, fg = ENTRY_FG)

            entry_label.pack(side = tk.LEFT)
            entry.pack(side = tk.LEFT)

            var_entries[var] = entry

        
        calc_button = tk.Button(variable_frame, text = CALC_BUTTON_LABEL, command = lambda: self.calculate(self.get_var_entry_input(var_entries)))
        calc_button.pack()

        self.root.geometry("")


    def get_var_entry_input(self, var_entries):
        var_inputs = {}
        for var in var_entries:
            var_inputs[var] = var_entries[var].get() 

        return var_inputs


    def calculate(self, var_inputs):
        self.calculate_observer.notify(var_inputs)    


    def display_result(self, result):
        frame = tk.Frame(self.root)
        frame.pack()
        
        label = tk.Label(frame, text = RESULT_LABEL + result)
        label.pack()

