import tkinter as tk
from tkinter import ttk
import requests


class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x420")
        self.root.configure(bg="teal")

        # ===== Title =====
        title = tk.Label(root, text="Currency Converter", 
                         font=("Arial", 16, "bold"),
                         bg="teal", fg="white")
        title.pack(pady=10)

        # ===== Amount =====
        self.amount_label = tk.Label(root, text="Amount:", 
                                     bg="teal", fg="white")
        self.amount_label.pack()

        self.enter_amount = tk.Entry(root, font=("Arial", 12))
        self.enter_amount.pack(pady=5)

        # ===== From Currency =====
        self.from_currency_label = tk.Label(root, text="From Currency:", 
                                            bg="teal", fg="white")
        self.from_currency_label.pack()

        self.from_currency_var = tk.StringVar()
        self.from_currency_dropdown = ttk.Combobox(
            root, textvariable=self.from_currency_var, state="readonly"
        )
        self.from_currency_dropdown['values'] = [
            "USD", "INR", "EUR", "JPY", "GBP", "AUD", "CAD", "SAR"
        ]
        self.from_currency_dropdown.current(1)  # Default INR
        self.from_currency_dropdown.pack(pady=5)

        # ===== To Currency =====
        self.to_currency_label = tk.Label(root, text="To Currency:", 
                                          bg="teal", fg="white")
        self.to_currency_label.pack()

        self.to_currency_var = tk.StringVar()
        self.to_currency_dropdown = ttk.Combobox(
            root, textvariable=self.to_currency_var, state="readonly"
        )
        self.to_currency_dropdown['values'] = [
            "USD", "INR", "EUR", "JPY", "GBP", "AUD", "CAD", "SAR"
        ]
        self.to_currency_dropdown.current(0)  # Default USD
        self.to_currency_dropdown.pack(pady=5)

        # ===== Convert Button =====
        self.convert_button = tk.Button(
            root, text="Convert", font=("Arial", 12, "bold"),
            command=self.convert_currency
        )
        self.convert_button.pack(pady=15)

        # ===== Result Label =====
        self.result_label = tk.Label(
            root, text="", font=("Arial", 12, "bold"),
            bg="teal", fg="yellow"
        )
        self.result_label.pack(pady=10)

    # ==============================
    # Currency Conversion Function
    # ==============================
    def convert_currency(self):
        try:
            amount = float(self.enter_amount.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            # Free Working API (2026)
            url = f"https://open.er-api.com/v6/latest/{from_currency}"
            response = requests.get(url)
            data = response.json()

            if data["result"] == "success":
                rate = data["rates"][to_currency]
                converted_amount = amount * rate

                self.result_label.config(
                    text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
                )
            else:
                self.result_label.config(text="Conversion failed!")

        except ValueError:
            self.result_label.config(text="Enter a valid number!")

        except Exception:
            self.result_label.config(text="Network Error! Check Internet.")


# ===== Run App =====
if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()