import os

# Get the current working directory
current_dir = os.getcwd()

# Define the command to execute the Python script without showing the terminal
command = f"python3 {os.path.join(current_dir, 'editor.py')}"

# Define the title and description for the shortcut
title = "Shortcut Editor"
description = "Python script for creating shortcuts in Linux."

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

print(f"Shortcut '{title}' created successfully at: {shortcut_file}")
