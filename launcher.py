import subprocess

# Define the list of Python files to execute
files_to_execute = [
    "ui_main_window.py",
    "video_server.py",
    "main.py"  # The main file to start the application
]

# Execute each file
for file in files_to_execute:
    print(f"Executing {file}...")
    subprocess.run(["python", file])

print("All files executed successfully.")
