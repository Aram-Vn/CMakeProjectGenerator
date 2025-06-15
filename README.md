# CMake Project Generator for C++

The CMake Project Generator is a Python script that automates the setup of modern C++ projects with CMake. It provides a consistent folder structure, generates essential configuration files, and includes a lightweight header-only logger utility for immediate use in development and debugging.

- [Scripts](#scripts)
- [Dependencies](#dependencies)
- [Features](#features)
- [Usage Adding to PATH](#adding-to-path)
  - [Steps](#steps)
  - [Using add_to_path.py After the First Run](#using-add_to_pathpy-after-the-first-run)
- [Usage of cppinit](#cppinit)
  - [With Project Name Argument](#with-project-name-argument)
  - [Without Project Name Argument](#without-project-name-argument)
  - [Example](#example)
  - [Logger](#logger)

## Scripts

- [cppinit](#cppinit): Generates the necessary files and directory structure for a new C++ project.
- [add_to_path.py](#adding-to-path): Copies the CMakeProjectGenerator.py script to a ~/scripts directory and updates your PATH environment variable to include this directory, allowing you to run the script from anywhere.

## Dependencies

- Python 3.x

## Features

- Creates a modular folder structure: `src`, `include`, `tests`, and `logger`.
- Generates `CMakeLists.txt` for root and test directories.
- Creates default `main.cpp`, `.h`, and `.cpp` files for your project.
- Includes a lightweight, header-only logger (`logger/logger.hpp`).
- Sets up `.gitignore` and `.clang-format`.
- Installs scripts globally via `~/scripts` and `PATH` integration.

## Adding to PATH

The `add_to_path.py` script copies a specified script (for example cppinit) to the `~/scripts` directory and adds this directory to your **PATH** environment variable, so you can execute the script from anywhere in the terminal.
If this is the first run, the `add_to_path.py` script will also copy itself to the `~/scripts` directory, removing the .py extension.

### Steps

if is first run

1. Ensure both scripts are in the same directory.
2. Run the add_to_path.py script with the name of the script you want to copy:

```bash
./add_to_path.py cppinit

# or

python add_to_path.py cppinit
```

This script will:

- Copy `cppinit` to ~/scripts.
- Check if ~/scripts is already in your PATH and add it to your .bashrc or .zshrc file if it is not.
- Instruct you to source your shell configuration file to update the PATH in the current session.

### Now you can run cppinit from any directory

```bash
cppinit <project_name>
```

## Using add_to_path.py After the First Run

After the first run, the `add_to_path.py` script is copied to the ~/scripts directory without the .py extension, allowing you to call it from anywhere:

```bash
add_to_path <script_name>
```

For example, to copy another script from any directory named `new_script` to the ~/scripts directory, so you can use it from anywhere:

```bash
add_to_path new_script
```

## cppinit

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
./cppinit
Please enter project name:
<project_name>
```

Result Structure

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
├── logger
│   ├── CMakeLists.txt
│   └── logger.hpp
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

## logger

This project includes a lightweight, header-only logging utility located in the `logger/` directory.

For full documentation, features, usage examples, and customization options, please visit the official repository:

🔗 [one_header_logger on GitHub](https://github.com/Aram-Vn/one_header_logger)

## Example Workflow

1. Generate a project:

```bash
cppinit MyProject
```

2. Navigate to your project directory:

```bash
cd MyProject
```

3. Build the project:

```bash
cd build
cmake ..
cmake --build .
```
