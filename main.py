import tkinter as tk
from tkinter import messagebox

# Function to calculate Simple Interest
def calculate_si(principal, time, rate):
    return (principal * time * rate) / 100

# Function to calculate Compound Interest
def calculate_ci(principal, time, rate):
    return principal * ((1 + rate / 100) ** time) - principal

# Function to handle calculation and display result
def calculate():
    try:
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())

        si = calculate_si(principal, time, rate)
        ci = calculate_ci(principal, time, rate)

        result_si.config(text=f"Simple Interest: {si:.2f}")
        result_ci.config(text=f"Compound Interest: {ci:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numerical values.")

# Main window
root = tk.Tk()
root.title("Interest Calculator")

# Labels and Entries for inputs
tk.Label(root, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=10)
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Time Period (years):").grid(row=1, column=0, padx=10, pady=10)
entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Rate of Interest (%):").grid(row=2, column=0, padx=10, pady=10)
entry_rate = tk.Entry(root)
entry_rate.grid(row=2, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Labels to display the results
result_si = tk.Label(root, text="Simple Interest: ")
result_si.grid(row=4, column=0, columnspan=2, pady=5)

result_ci = tk.Label(root, text="Compound Interest: ")
result_ci.grid(row=5, column=0, columnspan=2, pady=5)

# Start the application
root.mainloop()
