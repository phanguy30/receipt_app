import tkinter as tk
from gui import ReceiptGUI  # adjust the path if needed

def dummy_submit(data):
    print("Submitted data:")
    for k, v in data.items():
        print(f"{k}: {v}")

# List of dummy businesses
businesses = ["AN TAM", "MY SIDE HUSTLE"]

# Create the window
root = tk.Tk()
root.title("Receipt Generator")

# Create the GUI view
app = ReceiptGUI(root, businesses, dummy_submit)

# Show the window
root.mainloop()
