import tkinter as tk
from tkinter import ttk

class ReceiptGUI:
    def __init__(self, master, business_names, on_submit):
        self.master = master
        self.on_submit = on_submit

        self.fields = {}

        self._add_label_entry("Client Name", "client_name", 0)
        self._add_label_entry("Client Address", "client_address", 1)
        self._add_label_entry("Property Address", "property_address", 2)
        self._add_label_entry("Manager Name", "manager_name", 3, default="")
        self._add_label_entry("Term (e.g. May 2025)", "term", 4)
        self._add_label_entry("Invoice Number", "invoice_number", 5)

        tk.Label(master, text="Business").grid(row=6, column=0)
        self.business_var = tk.StringVar()
        self.business_dropdown = ttk.Combobox(master, textvariable=self.business_var, values=business_names)
        self.business_dropdown.grid(row=6, column=1)
        self.business_dropdown.set(business_names[0])

        tk.Button(master, text="Generate Receipt", command=self.submit).grid(row=7, column=0, columnspan=2)

    def _add_label_entry(self, label, key, row, default=""):
        tk.Label(self.master, text=label).grid(row=row, column=0)
        var = tk.StringVar(value=default)
        entry = tk.Entry(self.master, textvariable=var)
        entry.grid(row=row, column=1)
        self.fields[key] = var

    def submit(self):
        data = {key: var.get() for key, var in self.fields.items()}
        data["business_name"] = self.business_var.get()
        self.on_submit(data)
