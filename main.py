import tkinter as tk
from tkinter import messagebox

# Buttons layout as a global constant
BUTTONS = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]


class CalculatorApp:
    def __init__(self, root):
        """Initialize the application window and user interface components."""
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.current_expression = ""

        # Create the display entry widget
        self.display = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, ipadx=5, ipady=15)

        # Create calculator buttons
        for text, row, col in BUTTONS:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        """Create a button and place it in the specified row and column."""
        tk.Button(
            self.root,
            text=text,
            font=("Arial", 16),
            command=lambda: self.on_button_click(text)
        ).grid(row=row, column=col, ipadx=10, ipady=10, sticky="nsew")

    def on_button_click(self, text):
        """Handle button click events."""
        if text == "C":  # Clear the current expression
            self.current_expression = ""
        elif text == "=":  # Evaluate the current expression
            self.evaluate_expression()
        else:  # Append the button's text to the current expression
            self.current_expression += text
        self.update_display()

    def evaluate_expression(self):
        """Evaluate the mathematical expression entered by the user."""
        try:
            self.current_expression = str(eval(self.current_expression))  # Safely evaluate the expression
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed!")
            self.current_expression = ""
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression! {e}")
            self.current_expression = ""

    def update_display(self):
        """Update the calculator's display with the current expression."""
        self.display.delete(0, tk.END)  # Clear the display
        self.display.insert(0, self.current_expression)  # Insert the updated expression


if __name__ == "__main__":
    """Start the application by initializing the main window."""
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
