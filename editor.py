import os
import tkinter as tk
from tkinter import filedialog

def create_shortcut():
    # Get the command, title, and description from the entry fields
    command = command_entry.get()
    title = title_entry.get()
    description = description_entry.get("1.0", tk.END).strip()

    # Construct the contents of the .desktop file
    shortcut_content = f"""[Desktop Entry]
Name={title}
Exec={command}
Type=Application
Comment={description}
"""

    # Determine the path for the shortcut file
    desktop_dir = os.path.expanduser('~/.local/share/applications/')
    shortcut_file = os.path.join(desktop_dir, f"{title}.desktop")

    # Write the contents to the shortcut file
    with open(shortcut_file, 'w') as f:
        f.write(shortcut_content)

    # Display success message
    result_label.config(text=f"Shortcut '{title}' created successfully!")

def delete_shortcut():
    # Get the selected shortcut from the listbox
    selected_index = shortcut_listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        selected_shortcut = shortcut_listbox.get(selected_index)
        
        # Determine the path for the shortcut file
        desktop_dir = os.path.expanduser('~/.local/share/applications/')
        shortcut_file = os.path.join(desktop_dir, selected_shortcut)

        # Delete the shortcut file
        os.remove(shortcut_file)
        
        # Refresh the list of shortcuts
        refresh_shortcuts()

def refresh_shortcuts():
    # Clear the listbox
    shortcut_listbox.delete(0, tk.END)
    
    # Determine the directory containing the shortcuts
    desktop_dir = os.path.expanduser('~/.local/share/applications/')

    # List all files in the directory
    files = os.listdir(desktop_dir)

    # Iterate through each file
    for file_name in files:
        # Check if it's a file and ends with '.desktop'
        if os.path.isfile(os.path.join(desktop_dir, file_name)) and file_name.endswith('.desktop'):
            shortcut_listbox.insert(tk.END, file_name)

def browse_icon():
    # Open a file dialog to select an icon file
    icon_path = filedialog.askopenfilename(title="Select Icon File", filetypes=[("Icon files", "*.ico *.png *.jpg *.svg")])
    icon_path_entry.delete(0, tk.END)
    icon_path_entry.insert(0, icon_path)

# Create the main window
root = tk.Tk()
root.title("Shortcut Editor")
root.resizable(False, False)  # Disable resizing

# Create and place widgets
tk.Label(root, text="Command:").grid(row=0, column=0, sticky="w")
command_entry = tk.Entry(root, width=50)
command_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Title:").grid(row=1, column=0, sticky="w")
title_entry = tk.Entry(root, width=50)
title_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Description:").grid(row=2, column=0, sticky="w")
description_entry = tk.Text(root, width=50, height=5)
description_entry.grid(row=2, column=1, padx=5, pady=5)

create_button = tk.Button(root, text="Create Shortcut", command=create_shortcut)
create_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Create a second window for managing existing shortcuts
shortcut_window = tk.Toplevel(root)
shortcut_window.title("Manage Shortcuts")
shortcut_window.resizable(False, False)  # Disable resizing

# Create a listbox to display shortcuts
shortcut_listbox = tk.Listbox(shortcut_window, width=50, height=10)
shortcut_listbox.grid(row=0, column=0, padx=5, pady=5)

# Create buttons to delete and refresh shortcuts
delete_button = tk.Button(shortcut_window, text="Delete Selected Shortcut", command=delete_shortcut)
delete_button.grid(row=1, column=0, padx=5, pady=5)
refresh_button = tk.Button(shortcut_window, text="Refresh List", command=refresh_shortcuts)
refresh_button.grid(row=1, column=1, padx=5, pady=5)

# Refresh the list of shortcuts initially
refresh_shortcuts()

# Run the main event loop
root.mainloop()
