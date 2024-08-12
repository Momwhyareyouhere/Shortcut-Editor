import os
import tkinter as tk
from tkinter import filedialog

def create_shortcut():
    
    command = command_entry.get()
    title = title_entry.get()
    description = description_entry.get("1.0", tk.END).strip()

    
    shortcut_content = f"""[Desktop Entry]
Name={title}
Exec={command}
Type=Application
Comment={description}
"""

    
    desktop_dir = os.path.expanduser('~/.local/share/applications/')
    shortcut_file = os.path.join(desktop_dir, f"{title}.desktop")

    
    with open(shortcut_file, 'w') as f:
        f.write(shortcut_content)

    
    result_label.config(text=f"Shortcut '{title}' created successfully!")

def delete_shortcut():
    
    selected_index = shortcut_listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        selected_shortcut = shortcut_listbox.get(selected_index)
        
       
        desktop_dir = os.path.expanduser('~/.local/share/applications/')
        shortcut_file = os.path.join(desktop_dir, selected_shortcut)

        
        os.remove(shortcut_file)
        
        
        refresh_shortcuts()

def refresh_shortcuts():
    
    shortcut_listbox.delete(0, tk.END)
    
    
    desktop_dir = os.path.expanduser('~/.local/share/applications/')

    
    files = os.listdir(desktop_dir)

    
    for file_name in files:
        
        if os.path.isfile(os.path.join(desktop_dir, file_name)) and file_name.endswith('.desktop'):
            shortcut_listbox.insert(tk.END, file_name)

def browse_icon():
    
    icon_path = filedialog.askopenfilename(title="Select Icon File", filetypes=[("Icon files", "*.ico *.png *.jpg *.svg")])
    icon_path_entry.delete(0, tk.END)
    icon_path_entry.insert(0, icon_path)


root = tk.Tk()
root.title("Shortcut Editor")
root.resizable(False, False)  


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


shortcut_window = tk.Toplevel(root)
shortcut_window.title("Manage Shortcuts")
shortcut_window.resizable(False, False)  


shortcut_listbox = tk.Listbox(shortcut_window, width=50, height=10)
shortcut_listbox.grid(row=0, column=0, padx=5, pady=5)


delete_button = tk.Button(shortcut_window, text="Delete Selected Shortcut", command=delete_shortcut)
delete_button.grid(row=1, column=0, padx=5, pady=5)
refresh_button = tk.Button(shortcut_window, text="Refresh List", command=refresh_shortcuts)
refresh_button.grid(row=1, column=1, padx=5, pady=5)


refresh_shortcuts()


root.mainloop()
