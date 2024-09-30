import tkinter as tk

# Function to evaluate the expression
def calculate():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to input expression
entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

# StringVar to store result
result = tk.StringVar()
result.set("")

# Label to display result
result_label = tk.Label(root, textvariable=result, font=('Arial', 14), bg="white", width=20, anchor='e')
result_label.grid(row=1, column=0, columnspan=4)

# Buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Function to handle button clicks
def button_click(symbol):
    if symbol == 'C':
        entry.delete(0, tk.END)
        result.set("")
    elif symbol == '=':
        calculate()
    else:
        entry.insert(tk.END, symbol)

# Create and place buttons
for i, symbol in enumerate(buttons):
    row = i // 4 + 2
    col = i % 4
    button = tk.Button(root, text=symbol, font=('Arial', 14), width=4, height=2, command=lambda sym=symbol: button_click(sym))
    button.grid(row=row, column=col)

root.mainloop()
