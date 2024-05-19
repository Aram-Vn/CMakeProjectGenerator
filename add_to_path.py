#!/usr/bin/python

from typing import List
import sys
import os
import shutil
import stat

def copy_script_to_scripts(file_path: str) -> str:
    # Define destination directory
    dest_dir: str = os.path.expanduser("~/scripts")

    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Get the absolute path of the file to be copied
    source_path: str = os.path.abspath(file_path)
    file_name: str = os.path.basename(file_path)

    # Copy the script to the destination directory
    dest_path: str = os.path.join(dest_dir, file_name)
    shutil.copy(source_path, dest_path)

    # Make the script executable
    os.chmod(dest_path, os.stat(dest_path).st_mode | stat.S_IEXEC)

    print(f"Copied {file_name} to {dest_dir} and made it executable")

    return dest_path

def add_to_path(scripts_path: str) -> None:
    # Get the home directory
    home_dir: str = os.path.expanduser("~")

    # Check if the ~/.zshrc or ~/.bashrc exists
    rc_file: str = os.path.join(home_dir, ".zshrc")
    if not os.path.exists(rc_file):
        rc_file = os.path.join(home_dir, ".bashrc")

    # If neither .bashrc nor .zshrc exists, print a message and return
    if not os.path.exists(rc_file):
        print("Warning: Could not find ~/.bashrc or ~/.zshrc. Please add the following line manually:")
        print(f"export PATH=\"{scripts_path}:$PATH\"")
        return

    # Read the content of the rc file to check if the path already exists
    with open(rc_file, "r", encoding="utf-8") as file:
        rc_file_content: List[str] = file.readlines()
        
    path_exists: bool = any(f"export PATH=\"{scripts_path}:$PATH\"" in line for line in rc_file_content)

    if not path_exists:
        # Add the export command to the .bashrc or .zshrc file
        with open(rc_file, "a", encoding="utf-8") as file:
            file.write("\n# Added by make_env_variable.py script\n")
            file.write(f"export PATH=\"{scripts_path}:$PATH\"\n")

        print(f"Added {scripts_path} to PATH in {rc_file}")
        print("Please run the following command to update your current shell session:")
        print(f"source {rc_file}")
    else:
        print(f"The path {scripts_path} is already in the PATH variable in {rc_file}")

def main(argv: List[str]) -> None:
    argc: int = len(argv)
    file_path: str = ""

    if argc != 2:
        print("Enter file path:")
        file_path = input()
    else:
        file_path = argv[1]

    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        sys.exit(1)

    dest_path: str = copy_script_to_scripts(file_path)
    scripts_path: str = os.path.dirname(dest_path)
    add_to_path(scripts_path)

    # Check if this script is named 'add_to_path.py' and if it's the first run
    script_name = 'add_to_path.py'
    current_script_path = os.path.abspath(__file__)
    if not os.path.exists(os.path.join(os.path.expanduser("~/scripts"), script_name)):
        copy_script_to_scripts(current_script_path)

if __name__ == '__main__':
    main(sys.argv)
