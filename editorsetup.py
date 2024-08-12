import os


current_dir = os.getcwd()


command = f"python3 {os.path.join(current_dir, 'editor.py')}"


title = "Shortcut Editor"
description = "Python script for creating shortcuts in Linux."


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

print(f"Shortcut '{title}' created successfully at: {shortcut_file}")
