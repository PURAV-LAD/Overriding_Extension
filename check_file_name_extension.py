import tkinter as tk
from tkinter import filedialog, messagebox
import os

def check_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        initialdir=".",  # Initial directory
        filetypes=[("All files", "*.*")]  # Browse option
    )
    
    if not file_path:
        messagebox.showwarning("No File Selected", "Please select a file to Check.")
        return

    # Split file path into name and extension
    split_tup = os.path.splitext(os.path.basename(file_path))
    file_name = split_tup[0]
    file_extension = split_tup[1]

    # Show current file name and extension
    messagebox.showinfo("File Info", f"Current File Name: {file_name}\nCurrent File Extension: {file_extension}")

# Create the main window
root = tk.Tk()
root.title("File Name Overrider")
root.configure(bg='slateblue2')

# window size and position
window_width = 120
window_height = 100

# screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculating x and y coordinates for the window to be centered
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
# for centering used //(integer division)

# Setting window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Add a button to start the renaming process
rename_button = tk.Button(root, text="Check File", command=check_file, bg="palevioletred1", cursor="hand2")
rename_button.pack(padx=20, pady=30 , expand=True)

bold_font = ('Ariel', 10, 'bold')
coder_label = tk.Label(root, text="~Purav Lad", bg='slateblue2', fg='yellow' , font= bold_font)
coder_label.pack(side=tk.BOTTOM, anchor=tk.SE, padx=1, pady=1)

root.mainloop()
