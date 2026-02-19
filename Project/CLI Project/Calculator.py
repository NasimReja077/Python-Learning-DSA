import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("OOP GUI Calculator")
        self.root.geometry("320x420")
        self.root.resizable(False, False)

        self.expression = ""

        # Display Entry
        self.display = tk.Entry(
            root,
            font=("Arial", 20),
            borderwidth=5,
            relief="ridge",
            justify="right"
        )
        self.display.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # Button Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        # Button Layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create Buttons
        for (text, row, col) in buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                font=("Arial", 14),
                width=5,
                height=2,
                command=lambda t=text: self.on_click(t)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

        # Clear Button
        clear_btn = tk.Button(
            root,
            text="CLEAR",
            font=("Arial", 14),
            bg="red",
            fg="white",
            command=self.clear
        )
        clear_btn.pack(fill="both", padx=10, pady=10)

    # Button Click Handler
    def on_click(self, value):
        if value == "=":
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by Zero!")
                self.clear()
            except:
                messagebox.showerror("Error", "Invalid Expression")
                self.clear()
        else:
            self.expression += value
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    # Clear Display
    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)


# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
