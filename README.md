# CMake Project Generator for C++

The CMake Project Generator is a Python script that automates the setup of C++ projects with CMake, providing a consistent project structure and basic configuration files.

## Dependencies

- Python 3.x

## Features

- Generates CMakeLists.txt for the project root and test directories.
- reates a main.cpp file, a header file, and a source file.
- Configures .gitignore and .clang-format files for Git and code formatting.

## Usage

To use the CMake Project Generator, simply run the Python script with the project name as an argument:

```bash
./CMakeProjectGenerator.py <project_name>

# or 

python CMakeProjectGenerator.py <project_name>
```

or If you run the script without providing a project name as an argument, it will prompt you to enter the project name

```bash
./CMakeProjectGenerator.py

# or 

python CMakeProjectGenerator.py

```

You will then be prompted to enter the project name manually. After providing the project name, the script will proceed to create the project directory and files as usual.

## Adding to PATH

To make the CMakeProjectGenerator.py script executable from anywhere, you can add its directory to the PATH environment variable. You can do this by adding the following line to your .bashrc or .zshrc file:

```bash
export PATH="path/to/script/directory:$PATH"
```

Replace path/to/script/directory with the absolute path to the directory containing the script. After adding this line, you'll be able to run the script from any directory without specifying its full path.

## Result Structure

```bash
.
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
│   └── ProjectName.h
│
├── src/
│   └── ProjectName.cpp
│
└── tests/
    ├── ProjectName_test.cpp
    └── CMakeLists.txt
```