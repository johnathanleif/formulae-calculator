import tkinter as tk
from tkinter import ttk


WINDOW_TITLE = "Formulae Calculator"
FORMULA_ENTRY_TEXT = "Input Formula: "
PARSE_BUTTON_TEXT = "Parse" 
CALC_BUTTON_TEXT = "Calculate"
VAR_TEXT = " = "
RESULT_TEXT = "Result = "

ENTRY_BG = "white"
ENTRY_FG = "black"

VARIABLE_ENTRY_COLUMNS = 2

class TkView(tk.Tk):

    def __init__(self, parse_observer, calculate_observer):
        super().__init__(None)
        self.title(WINDOW_TITLE)
        self.parse_observer = parse_observer
        self.calculate_observer = calculate_observer


    def open_window(self):
        self.create_formula_input()
        self.mainloop()


    def create_formula_input(self):
        frame = tk.Frame(self)
        frame.pack()

        entry_label = tk.Label(frame, text = FORMULA_ENTRY_TEXT)
        entry = tk.Entry(frame, bg = ENTRY_BG, fg = ENTRY_FG)
        parse_button = tk.Button(frame, text = PARSE_BUTTON_TEXT, command = lambda: self.__parse(entry.get()))

        entry_label.pack(side = tk.LEFT)
        entry.pack(side = tk.LEFT)
        parse_button.pack(side = tk.RIGHT)

        self.__resize()

    
    def create_variable_input(self, variables):
        self.__create_separator()

        variable_frame = tk.Frame(self)
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

            entry_label = tk.Label(frame, text = var + VAR_TEXT) 
            entry = tk.Entry(frame, bg = ENTRY_BG, fg = ENTRY_FG)

            entry_label.pack(side = tk.LEFT)
            entry.pack(side = tk.LEFT)

            var_entries[var] = entry

        
        calc_button = tk.Button(variable_frame, text = CALC_BUTTON_TEXT, command = lambda: self.__calculate(self.__get_var_entry_input(var_entries)))
        calc_button.pack()

        self.__resize()


    def display_result(self, result):
        self.__create_separator()
        frame = tk.Frame(self)
        frame.pack()
        
        label = tk.Label(frame, text = RESULT_TEXT + result)
        label.pack()
        
        self.__resize()
 
    
    def __create_separator(self):
        separator = ttk.Separator(self)
        separator.pack(fill = 'x')
    
    
    def __resize(self):
        self.geometry('')
    

    def __parse(self, input_formula_string):
        self.parse_observer.notify(input_formula_string)


    def __calculate(self, var_inputs):
        self.calculate_observer.notify(var_inputs)    

    @staticmethod
    def __get_var_entry_input(var_entries):
        var_inputs = {}
        for var in var_entries:
            var_inputs[var] = var_entries[var].get() 

        return var_inputs    
   
