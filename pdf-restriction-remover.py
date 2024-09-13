import tkinter as tk
from tkinter import filedialog, messagebox
import pikepdf

# Function to remove restrictions from the PDF
def unlock_pdf():
    try:
        # Get the selected file and password from the user
        input_pdf_path = filedialog.askopenfilename(title="Select PDF", filetypes=[("PDF Files", "*.pdf")])
        if not input_pdf_path:
            return
        
        pdf_password = password_entry.get()
        
        # Open the PDF with the provided password
        with pikepdf.open(input_pdf_path, password=pdf_password) as pdf:
            # Create a save dialog to get the output file path
            output_pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if not output_pdf_path:
                return

            # Save the PDF without restrictions
            pdf.save(output_pdf_path)
            messagebox.showinfo("Success", f"Restrictions removed successfully! Saved as: {output_pdf_path}")
    except pikepdf._qpdf.PasswordError:
        messagebox.showerror("Error", "Incorrect password or unable to open the PDF.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the main window
root = tk.Tk()
root.title("PDF Restriction Remover")
root.geometry("400x200")

# Create the interface
tk.Label(root, text="PDF Password:", font=("Arial", 12)).pack(pady=10)

password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

unlock_button = tk.Button(root, text="Select PDF and Remove Restrictions", font=("Arial", 12), command=unlock_pdf)
unlock_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
