import tkinter as tk
import tkinter.messagebox as tkmessagebox
#very important, tkinter is gui interface for python
#when using anythin from tkinter/tkinter.messagebox the 'as tk/tkmessagebox' is how you reference the objects from each module
#gui canvas size for start up as predefined variables
Can_height = 600
Can_width = 600

#calculations for final wage
def Wage_calculation():
    Wage_ph = 0
    hours_pw = 0
    tax_code = 0
    final_wage= 0
    taxed_income = 0
#can explain how to get the wage, hours etc in further detail if needed

#tax code function for inputting into the lists and calculations
def Tax_code():
    #tax codes
    print(8)
#main menu to display gui first
def main_menu():
    
    #starting main window
    win = tk.Tk()
    #win value very important, provides parent object for other objects
    win.minsize(400,400)
    #window minimum size in pixels, think there is a maxsize aswell
    canvas  = tk.Canvas(win, height = Can_height, width = Can_width)
    canvas.pack()
    #pack shows objects in block form, e.g word inline-block
    #within tk.canvas win is the parent object
    #when using Canvas, frame, label etc the tk. is required as the . allows python to see you are referencing another function/module
    
    title_label = tk.Label(win, text="Wage calculator", font=36)
    title_label.place(relx=0.5, rely=0.05, anchor='center')
    #place shows objects in pre-defined relative spots e.g relx == relative x coordinate
    #relx is the relative x within the parent object ranges for relative values are 0-1
    #rely is the relative y within the parent object
    #anchor is basically the 'allignment' of the text within/ the object itself, the codes for that is the NESW and center 
    
    #frame for grouping all entries
    entry_frame = tk.Frame(win, bg='gray', bd=5)
    entry_frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.25, anchor='n')
    #bg is background colour, can use regular python 'colors' or hex codes for colours e.g. #FFFFF for white, useful to quote colours for later searching
    
    #frame for grouping hourly wage
    Hourly_wage_frame = tk.Frame(entry_frame, bg='blue', bd=2)
    Hourly_wage_frame.place(relx=0.01, rely=0.01, relwidth=0.99, relheight=0.30)
    
    hourly_wage_label = tk.Label(Hourly_wage_frame, text="Hourly wage", font=32)
    hourly_wage_label.place(relx=0.01, relwidth=0.5, relheight=1)
    #text displayed within ""
    
    hourly_wage_entry = tk.Entry(Hourly_wage_frame, font=32)
    hourly_wage_entry.place(relx=0.55, relwidth=0.45, relheight=1)
    
    #frame for grouping all hours worked
    hours_worked_frame = tk.Frame(entry_frame, bg='blue', bd=2)
    hours_worked_frame.place(relx=0.01, rely=0.35, relwidth=0.99, relheight=0.30)
    #bd is border, values are in pixels
    
    hours_worked_label = tk.Label(hours_worked_frame, text='Hours Worked', font=32)
    hours_worked_label.place(relx=0.01, relwidth=0.5, relheight=1)
    
    hours_worked_entry = tk.Entry(hours_worked_frame, font=32)
    hours_worked_entry.place(relx=0.55, relwidth=0.45, relheight=1)
    
    #frame for grouping tax codes
    tax_code_frame = tk.Frame(entry_frame, bg='blue', bd=2)
    tax_code_frame.place(relx=0.01, rely=0.7, relwidth=0.99, relheight=0.30)
    
    tax_code_label = tk.Label(tax_code_frame, text="Tax Code", font=32)
    tax_code_label.place(relx=0.01, relwidth=0.5, relheight=1)
    
    tax_code_lstbox = tk.Listbox(tax_code_frame, font=32)
    tax_code_lstbox.place(relx=0.55, relwidth=0.45, relheight=1)
    
    #frame for outputted data
    output_frame = tk.Frame(win, bg='gray', bd=5)
    output_frame.place(relx=0.5, rely=0.36, relwidth=0.8, relheight=0.25, anchor='n')
    
    output_button = tk.Button(output_frame, text="Calculate income", font=32, command= Wage_calculation)
    output_button.place(relx=0.01,rely=0.01, relwidth=0.99)
    #command= is the referencing of other functions within the program, here its wage calculation but could be any other function
    
    tkmessagebox.showinfo("answer")
    #the messagebox is a windows alert messagebox, useful to put all text in speech marks for ease of reading
    
    #closing main window
    win.mainloop()
    
    

#essential functions to be loaded on program launch
main_menu()