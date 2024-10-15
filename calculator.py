import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

# Entry widget to display expressions and results
expression = ""
input_text = tk.StringVar()

input_frame = tk.Frame(window)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18), width=25, bd=5, insertwidth=4, bg="powder blue", justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of input field

# Function to update expression in the input field
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to evaluate the final expression
def btn_equal():
    try:
        global expression
        result = str(eval(expression))  # 'eval' to evaluate the string expression
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

# Function to clear the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# Creating button frame
btns_frame = tk.Frame(window)
btns_frame.pack()

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Loop to create buttons and place them in the grid
for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        if button == "=":
            tk.Button(btns_frame, text=button, width=10, height=3, command=btn_equal).grid(row=i, column=j, padx=5, pady=5)
        elif button == "C":
            tk.Button(btns_frame, text=button, width=10, height=3, command=btn_clear).grid(row=i, column=j, padx=5, pady=5)
        else:
            tk.Button(btns_frame, text=button, width=10, height=3, command=lambda b=button: btn_click(b)).grid(row=i, column=j, padx=5, pady=5)

# Start the GUI event loop
window.mainloop()
