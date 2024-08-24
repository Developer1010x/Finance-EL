import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
import numpy as np
import json
import csv

# Define the main application class
class FinancialAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Financial Analysis Tool")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for Exchange Rate Risk Simulation
        ttk.Label(self.root, text="Exchange Rate Risk Simulation").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.root, text="Revenue (CNY):").grid(row=1, column=0, sticky="e")
        self.revenue_cny = ttk.Entry(self.root)
        self.revenue_cny.grid(row=1, column=1)

        ttk.Label(self.root, text="Initial CNY/USD Rate:").grid(row=2, column=0, sticky="e")
        self.initial_rate = ttk.Entry(self.root)
        self.initial_rate.grid(row=2, column=1)

        ttk.Label(self.root, text="New CNY/USD Rate:").grid(row=3, column=0, sticky="e")
        self.new_rate = ttk.Entry(self.root)
        self.new_rate.grid(row=3, column=1)

        ttk.Button(self.root, text="Simulate Exchange Rate Impact", command=self.simulate_exchange_rate_impact).grid(row=4, column=0, columnspan=2, pady=10)

        # Labels and Entries for Hedging with Forward Contracts
        ttk.Label(self.root, text="Hedging with Forward Contracts").grid(row=5, column=0, columnspan=2, pady=10)

        ttk.Label(self.root, text="Hedged Percentage:").grid(row=6, column=0, sticky="e")
        self.hedged_percentage = ttk.Entry(self.root)
        self.hedged_percentage.grid(row=6, column=1)

        ttk.Label(self.root, text="Forward Contract Rate:").grid(row=7, column=0, sticky="e")
        self.forward_rate = ttk.Entry(self.root)
        self.forward_rate.grid(row=7, column=1)

        ttk.Button(self.root, text="Calculate Hedged Revenue", command=self.calculate_hedged_revenue).grid(row=8, column=0, columnspan=2, pady=10)

        # Labels and Entries for NPV Calculation
        ttk.Label(self.root, text="Net Present Value (NPV) Calculation").grid(row=9, column=0, columnspan=2, pady=10)

        ttk.Label(self.root, text="Discount Rate:").grid(row=10, column=0, sticky="e")
        self.discount_rate = ttk.Entry(self.root)
        self.discount_rate.grid(row=10, column=1)

        ttk.Label(self.root, text="Cash Flows (comma-separated):").grid(row=11, column=0, sticky="e")
        self.cash_flows = ttk.Entry(self.root)
        self.cash_flows.grid(row=11, column=1)

        ttk.Button(self.root, text="Calculate NPV", command=self.calculate_npv).grid(row=12, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Plot Cash Flows", command=self.plot_cash_flows).grid(row=12, column=2, pady=10)

        # Labels and Entries for Political Risk Insurance
        ttk.Label(self.root, text="Political Risk Insurance Calculation").grid(row=13, column=0, columnspan=2, pady=10)

        ttk.Label(self.root, text="Investment Amount:").grid(row=14, column=0, sticky="e")
        self.investment = ttk.Entry(self.root)
        self.investment.grid(row=14, column=1)

        ttk.Label(self.root, text="Premium Rate:").grid(row=15, column=0, sticky="e")
        self.premium_rate = ttk.Entry(self.root)
        self.premium_rate.grid(row=15, column=1)

        ttk.Button(self.root, text="Calculate Insurance Cost", command=self.calculate_political_risk_insurance).grid(row=16, column=0, columnspan=2, pady=10)

        # Labels and Entries for Interest Cost Savings
        ttk.Label(self.root, text="Interest Cost Savings Calculation").grid(row=17, column=0, columnspan=2, pady=10)

        ttk.Label(self.root, text="Capital Amount:").grid(row=18, column=0, sticky="e")
        self.capital_amount = ttk.Entry(self.root)
        self.capital_amount.grid(row=18, column=1)

        ttk.Label(self.root, text="Domestic Rate:").grid(row=19, column=0, sticky="e")
        self.domestic_rate = ttk.Entry(self.root)
        self.domestic_rate.grid(row=19, column=1)

        ttk.Label(self.root, text="Eurobond Rate:").grid(row=20, column=0, sticky="e")
        self.eurobond_rate = ttk.Entry(self.root)
        self.eurobond_rate.grid(row=20, column=1)

        ttk.Button(self.root, text="Calculate Interest Savings", command=self.calculate_interest_savings).grid(row=21, column=0, columnspan=2, pady=10)

        # Additional Buttons for File Operations and Currency Conversion
        ttk.Button(self.root, text="Save Data", command=self.save_data).grid(row=22, column=0, pady=10)
        ttk.Button(self.root, text="Load Data", command=self.load_data).grid(row=22, column=1, pady=10)
        ttk.Button(self.root, text="Convert Currency", command=self.convert_currency).grid(row=22, column=2, pady=10)

    def simulate_exchange_rate_impact(self):
        try:
            revenue_cny = float(self.revenue_cny.get())
            initial_rate = float(self.initial_rate.get())
            new_rate = float(self.new_rate.get())

            revenue_usd_initial = revenue_cny / initial_rate
            revenue_usd_new = revenue_cny / new_rate
            impact = revenue_usd_new - revenue_usd_initial

            messagebox.showinfo("Exchange Rate Impact",
                                f"Initial Revenue in USD: ${revenue_usd_initial:.2f}\n"
                                f"New Revenue in USD: ${revenue_usd_new:.2f}\n"
                                f"Impact of Exchange Rate Change: ${impact:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

    def calculate_hedged_revenue(self):
        try:
            revenue_cny = float(self.revenue_cny.get())
            hedged_percentage = float(self.hedged_percentage.get())
            forward_rate = float(self.forward_rate.get())
            initial_rate = float(self.initial_rate.get())

            hedged_revenue = revenue_cny * hedged_percentage / forward_rate
            unhedged_revenue = revenue_cny * (1 - hedged_percentage) / initial_rate
            total_revenue = hedged_revenue + unhedged_revenue

            messagebox.showinfo("Hedged Revenue",
                                f"Total Revenue with Hedging: ${total_revenue:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

    def calculate_npv(self):
        try:
            discount_rate = float(self.discount_rate.get())
            cash_flows = list(map(float, self.cash_flows.get().split(',')))

            npv = sum(cf / (1 + discount_rate) ** t for t, cf in enumerate(cash_flows))

            messagebox.showinfo("NPV Calculation",
                                f"NPV of Project: ${npv:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers and ensure cash flows are comma-separated.")

    def plot_cash_flows(self):
        try:
            cash_flows = list(map(float, self.cash_flows.get().split(',')))
            plt.plot(range(len(cash_flows)), cash_flows, marker='o')
            plt.title("Cash Flows Over Time")
            plt.xlabel("Year")
            plt.ylabel("Cash Flow")
            plt.grid(True)
            plt.show()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid cash flows.")

    def calculate_political_risk_insurance(self):
        try:
            investment = float(self.investment.get())
            premium_rate = float(self.premium_rate.get())

            insurance_coverage = investment * 0.9
            annual_premium = investment * premium_rate

            messagebox.showinfo("Political Risk Insurance",
                                f"Insurance Coverage: ${insurance_coverage:.2f}\n"
                                f"Annual Premium Cost: ${annual_premium:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for investment and premium rate.")

    def calculate_interest_savings(self):
        try:
            amount = float(self.capital_amount.get())
            domestic_rate = float(self.domestic_rate.get())
            eurobond_rate = float(self.eurobond_rate.get())

            domestic_cost = amount * domestic_rate
            eurobond_cost = amount * eurobond_rate
            savings = domestic_cost - eurobond_cost

            messagebox.showinfo("Interest Savings",
                                f"Interest Savings from Eurobonds: ${savings:.2f} annually")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for capital amount, domestic rate, and Eurobond rate.")

    def save_data(self):
        try:
            data = {
                "exchange_rate": {
                    "revenue_cny": self.revenue_cny.get(),
                    "initial_rate": self.initial_rate.get(),
                    "new_rate": self.new_rate.get()
                },
                "hedging": {
                    "hedged_percentage": self.hedged_percentage.get(),
                    "forward_rate": self.forward_rate.get()
                },
                "npv": {
                    "discount_rate": self.discount_rate.get(),
                    "cash_flows": self.cash_flows.get()
                },
                "insurance": {
                    "investment": self.investment.get(),
                    "premium_rate": self.premium_rate.get()
                },
                "interest_savings": {
                    "capital_amount": self.capital_amount.get(),
                    "domestic_rate": self.domestic_rate.get(),
                    "eurobond_rate": self.eurobond_rate.get()
                }
            }

            file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                   filetypes=[("JSON files", "*.json")])
            if file_path:
                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=4)
                messagebox.showinfo("Save Data", "Data saved successfully.")
        except Exception as e:
            messagebox.showerror("Save Error", f"An error occurred while saving data: {e}")

    def load_data(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
            if file_path:
                with open(file_path, 'r') as file:
                    data = json.load(file)

                self.revenue_cny.delete(0, tk.END)
                self.revenue_cny.insert(0, data["exchange_rate"]["revenue_cny"])

                self.initial_rate.delete(0, tk.END)
                self.initial_rate.insert(0, data["exchange_rate"]["initial_rate"])

                self.new_rate.delete(0, tk.END)
                self.new_rate.insert(0, data["exchange_rate"]["new_rate"])

                self.hedged_percentage.delete(0, tk.END)
                self.hedged_percentage.insert(0, data["hedging"]["hedged_percentage"])

                self.forward_rate.delete(0, tk.END)
                self.forward_rate.insert(0, data["hedging"]["forward_rate"])

                self.discount_rate.delete(0, tk.END)
                self.discount_rate.insert(0, data["npv"]["discount_rate"])

                self.cash_flows.delete(0, tk.END)
                self.cash_flows.insert(0, data["npv"]["cash_flows"])

                self.investment.delete(0, tk.END)
                self.investment.insert(0, data["insurance"]["investment"])

                self.premium_rate.delete(0, tk.END)
                self.premium_rate.insert(0, data["insurance"]["premium_rate"])

                self.capital_amount.delete(0, tk.END)
                self.capital_amount.insert(0, data["interest_savings"]["capital_amount"])

                self.domestic_rate.delete(0, tk.END)
                self.domestic_rate.insert(0, data["interest_savings"]["domestic_rate"])

                self.eurobond_rate.delete(0, tk.END)
                self.eurobond_rate.insert(0, data["interest_savings"]["eurobond_rate"])

                messagebox.showinfo("Load Data", "Data loaded successfully.")
        except Exception as e:
            messagebox.showerror("Load Error", f"An error occurred while loading data: {e}")

    def convert_currency(self):
        try:
            amount = float(self.revenue_cny.get())
            rate = float(self.initial_rate.get())
            converted_amount = amount / rate  # Assuming conversion to USD
            messagebox.showinfo("Currency Conversion",
                                f"Converted Amount in USD: ${converted_amount:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for conversion.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialAnalysisApp(root)
    root.mainloop()
