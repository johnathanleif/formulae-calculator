import tkinter as tk

numbers = ["1","2","3","4","5","6","7","8","9","0"]
operators = ['+', '-', '*', '/', '(', ')', '^']

var_pos = {}
var_entry = {}
var_label_entry = {}
entry_list = []
positions = []

parse_widgets = []
calc_widgets = []


class Application(tk.Frame):


    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()



    def create_widgets(self):
        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text = "Parse", command = self.parse)
        self.button.pack()


    def parse(self):

        #-- GUI Code  --

        self.remove_widgets(parse_widgets)
        self.remove_widgets(calc_widgets)

        try:    
            calc_button
        except:
            pass
        else:
            calc_button.pack_forget()

        #-- End GUI Code --

        global string
        string = self.entry.get();

        var_list = []
        var_name = "";
        
        for i in range(len(string)):
            if string[i] in ['+', '-', '*', '/', '(', ')', '^']:               #if sign
                pass
            elif string[i] == ' ':                              #if space
                pass
            elif string[i] in numbers and var_name == "":       #if number not following a variable
                pass
            else:
                if i+1 < len(string) and string[i+1] not in operators + [' ']:      #if not last character and next character is not a sign or a space
                    var_name += string[i]
                    continue
                elif i+1 > len(string) and var_name != "":                                  #if last character and following a variable
                    var_name += string[i]
                    var_list.append(var_name)

                    self.update_variable_position(var_name, i - len(var_name) + 1)
            
                    var_name = ""
                    

                if var_name == "":      #if not following a variable
                    var_list.append(string[i])

                    self.update_variable_position(string[i], i)

                else:
                    var_name += string[i]
                    var_list.append(var_name)

                    self.update_variable_position(var_name, i - len(var_name) + 1)
                    
                    var_name = ""

        print(var_list)
        self.create_var_entries(var_list)

    
    def update_variable_position(self, var_name, var_index):
        if var_name in var_pos:
            var_pos[var_name].append(var_index)
        else:
            var_pos[var_name] = [var_index]

    
    def create_var_entries(self, variables):
       
        for i in range(len(variables)):
            label = tk.Label(self, text=variables[i])
            label.pack()
            parse_widgets.append(label)
            
            entry = tk.Entry(self)
            entry.pack()
            parse_widgets.append(entry)
            
            var_entry.update({variables[i]: entry})
            

        global calc_button
        calc_button = tk.Button(self, text="Calculate", command=self.calculate)
        calc_button.pack()
        

    def calculate(self):

        string_list = list(string)
        modifier = 0
      
        for i in var_pos:
            print("i=" + str(i))
            positions = var_pos[i]
            
            for j in positions:
                
                print("j=" + str(j))
                if i in var_entry and type(i) is not None:

                    number = var_entry[i].get()
                    
                    string_list[j-modifier: (j-modifier)+len(i)] = number

                    modifier += len(i) - len(number)

        print(string_list)
        print("".join(string_list))
        str_lst_str = "".join(string_list)
        str_lst_str = str_lst_str.replace(" ", "")
        str_lst_str = str_lst_str.replace("^", "**")

        #code = compile(str_lst_str, "<string>", "eval")
        #result = eval(code)
        result = eval(str_lst_str)
        print(str_lst_str)
        print(result)

        eval_string = str(eval(str_lst_str))

        #-- GUI Code --

        self.remove_widgets(calc_widgets)
        
        global result_label
        result_label = tk.Label(self, text="Result = " + eval_string)
        result_label.pack()

        if result_label not in calc_widgets:
            calc_widgets.append(result_label)


    def remove_widgets(self, widget_list):
        for widget in widget_list:
            widget.pack_forget()


app = Application(master=tk.Tk())
app.mainloop()
