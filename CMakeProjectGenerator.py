#!/usr/bin/python

import os
# import platform
# from enum import Enum

project_name: str = "test"


#________________________________-main_cpp-________________________________#
main_cpp_content: str = f"""
#include <iostream>
#include <{project_name}.h>

int main()
{{
    my::A a{{}};
    std::cout << "YES " << a.p << std::endl;
    return 0;
}}
"""

#________________________________-header_file-________________________________#
header_file_content: str = f"""
#ifndef {project_name.upper()}_INCLUDE_{project_name.upper()}_H
#define {project_name.upper()}_INCLUDE_{project_name.upper()}_H

namespace my {{
    class A {{
    public:
    A();

    int p;
    }};
}} // namespace my

#endif // {project_name.upper()}_INCLUDE_{project_name.upper()}_H
"""

#________________________________-src_file-________________________________#
src_file_content: str = f"""
#include "../include/{project_name}.h"

namespace my {{
    A::A() : p(42) {{}}
}} // namespace my
"""


#________________________________-.git_ignore_content-________________________________#
git_ignore_content: str = """
build/
compile_commands.json
.clang-format
.vscode
.cache
"""

#________________________________-.CMakeLists.txt__root-________________________________#
Cmake_list_root: str = f"""
cmake_minimum_required(VERSION 3.10)

project("{project_name}")
set(CMAKE_EXPORT_COMPILE_COMMANDS on)

file(GLOB_RECURSE SRC_FILES "src/*.cpp")
file(GLOB_RECURSE HDR_FILES "src/*.h")

add_executable("{project_name}" main.cpp  ${{SRC_FILES}} ${{HDR_FILES}})

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

target_include_directories("{project_name}" PRIVATE ${{CMAKE_CURRENT_SOURCE_DIR}}/include)

add_subdirectory(tests)

target_compile_options("{project_name}" PRIVATE 
    -Wall
    -Wextra
    -Wshadow
    -Wswitch
    -pedantic
    -Wformat=2
    -Wconversion
    -Wnull-dereference
    -Wunused-parameter
    -Wunreachable-code
    -Wimplicit-fallthrough
    
    -Werror
    -Werror=return-type
    -Werror=uninitialized
    -Werror=unused-result
    -Werror=strict-overflow
   
    -fsanitize=address
    -fsanitize=undefined
   
    -fno-omit-frame-pointer
)

target_link_options("{project_name}" PRIVATE 
    -fsanitize=address
    -fsanitize=undefined
)

target_compile_features("{project_name}" PRIVATE cxx_std_20)
"""

#________________________________-.CMakeLists.txt__test-________________________________#
Cmake_list_test_content: str = f"""
cmake_minimum_required(VERSION 3.10)

project({project_name}_test)

find_package(GTest REQUIRED)

include_directories(${{GTEST_INCLUDE_DIRS}})
include_directories(${{CMAKE_SOURCE_DIR}}/include)  


add_executable({project_name}_test {project_name}_test.cpp)

target_include_directories({project_name}_test PRIVATE ${{CMAKE_SOURCE_DIR}}/include)
target_link_libraries({project_name}_test ${{GTEST_LIBRARIES}} ${{GTEST_MAIN_LIBRARIES}} pthread)

enable_testing()
add_test(NAME {project_name}_test COMMAND {project_name}_test)
target_compile_options({project_name}_test PRIVATE -Wall)
"""

test_file_content: str = f"""
#include <{project_name}.h>
#include <gtest/gtest.h>

TEST({project_name}Test, {project_name}Test__1) 
{{}}

int main(int argc, char** argv)
{{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}}

"""

#________________________________-.clang-format-________________________________#
clang_format_conten: str = """
Language: Cpp
BasedOnStyle: Microsoft
AlignTrailingComments: true
BreakBeforeBraces: Custom
BraceWrapping:
    AfterEnum: true
    AfterStruct: true
    AfterClass: true
    AfterFunction: true
    AfterUnion: true
    AfterExternBlock: false
    BeforeCatch: true
    BeforeElse: true
    BeforeLambdaBody: true
    BeforeWhile: false
    AfterNamespace: false
    SplitEmptyFunction: true
IndentWidth: 4
KeepEmptyLinesAtTheStartOfBlocks: false
PointerBindsToType: true
SpacesBeforeTrailingComments: 1
TabWidth: 4
UseTab: Never
IndentCaseLabels: true
NamespaceIndentation: All
AccessModifierOffset: -4
AlignAfterOpenBracket: Align
AlignConsecutiveAssignments: Consecutive
AlignConsecutiveMacros:
    Enabled: true
    AcrossEmptyLines: true
    AcrossComments: false
AllowShortCaseLabelsOnASingleLine: true
AlignEscapedNewlines: Right
AllowShortBlocksOnASingleLine: Always
AllowShortEnumsOnASingleLine: false
AlignConsecutiveDeclarations: true
AlwaysBreakTemplateDeclarations: true
Cpp11BracedListStyle: false
PackConstructorInitializers: Never
AllowShortFunctionsOnASingleLine: Empty
ReflowComments: true
PenaltyBreakComment: 0
PenaltyBreakOpenParenthesis: 1
"""

def write_file(file_path: str, content: str = "") -> None:
    with open(file_path, "w") as fs:
        fs.write(content)

def main() -> None:

    os.makedirs(project_name, exist_ok=True)

    write_file(os.path.join(project_name, "main.cpp"), main_cpp_content)
    write_file(os.path.join(project_name, ".clang-format"), clang_format_conten)
    write_file(os.path.join(project_name, ".gitignore"), git_ignore_content)
    write_file(os.path.join(project_name, "CMakeLists.txt"), Cmake_list_root)    
    
            
    os.makedirs(os.path.join(project_name, "build"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "src"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "include"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "tests"), exist_ok=True)
    
    write_file(os.path.join(project_name, "src",  f'{project_name}.cpp'), src_file_content)
    write_file(os.path.join(project_name, "include",  f'{project_name}.h'), header_file_content)
    
    write_file(os.path.join(project_name,  "tests", f'{project_name}_test.cpp'), test_file_content)
    write_file(os.path.join(project_name,  "tests", "CMakeLists.txt"), Cmake_list_test_content)
    
if __name__ == '__main__':
    main()