import tkinter as tk

def on_click(button_text):
    current = display.get()
    if button_text == "C":
        display.delete(0, tk.END)  # Clear the display
    elif button_text == "=":
        try:
            result = eval(current)  # Evaluate the expression
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, button_text)  # Add button text to display

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the display entry box
display = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=5, relief="ridge")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Add buttons to the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Start the main loop
root.mainloop()

