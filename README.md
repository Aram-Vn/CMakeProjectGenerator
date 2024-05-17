# CMake Project Generator for C++

The CMake Project Generator is a Python script that automates the setup of C++ projects with CMake, providing a consistent project structure and basic configuration files.

## Scripts

- [cppinit](#usage): Generates the necessary files and directory structure for a new C++ project.
- [add_to_path.py](#adding-to-path): Copies the CMakeProjectGenerator.py script to a ~/scripts directory and updates your PATH environment variable to include this directory, allowing you to run the script from anywhere.

## Dependencies

- Python 3.x

## Features

- Generates CMakeLists.txt for the project root and test directories.
- reates a main.cpp file, a header file, and a source file.
- Configures .gitignore and .clang-format files for Git and code formatting.

## Usage

### With Project Name Argument

To use the cppinit, simply run the Python script with the project name as an argument:

```bash
./cppinit <project_name>

# or 

python cppinit <project_name>
```

### Without Project Name Argument

or If you run the script without providing a project name as an argument, it will prompt you to enter the project name

```bash
./cppinit

# or 

python cppinit

```

You will then be prompted to enter the project name manually. After providing the project name, the script will proceed to create the project directory and files as usual.

### Example

```bash
$ ./cppinit
Please enter project name:
MyProject
```

## Adding to PATH

The add_to_path.py script copies script(for example cppinit) to the ~/scripts directory and adds this directory to your PATH environment variable, so you can execute the script from anywhere in the terminal.

### Steps

1. Ensure both scripts are in the same directory.
2. Run the add_to_path.py script with the name of the script you want to copy:

```bash
./add_to_path.py <script name>

# or

python add_to_path.py <script name>
```

This script will:

- Copy `script name` to ~/scripts.
- Check if ~/scripts is already in your PATH and add it to your .bashrc or .zshrc file if it is not.
- Instruct you to source your shell configuration file to update the PATH in the current session.

## Result Structure

```bash
<project_name>/
├── main.cpp
│
├── .clang-format
│
├── .gitignore
│
├── CMakeLists.txt
│
├── build/
│
├── include/
│   └── <project_name>.h
│
├── src/
│   └── <project_name>.cpp
│
└── tests/
    ├── <project_name>_test.cpp
    └── CMakeLists.txt
```