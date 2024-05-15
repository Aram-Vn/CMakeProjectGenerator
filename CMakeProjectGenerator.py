#!/usr/bin/python

import os
# import platform
# from enum import Enum

class ProjectContent:
    def __init__(self, project_name: str):
        self.projectName = project_name
        #________________________________-main_cpp-________________________________#
        self.main_cpp_content: str = f"""
        #include <iostream>
        #include <{self.projectName}.h>

        int main()
        {{
            my::A a{{}};
            std::cout << "YES " << a.p << std::endl;
            return 0;
        }}
        """

        #________________________________-header_file-________________________________#
        self.header_file_content: str = f"""
        #ifndef {self.projectName.upper()}_INCLUDE_{self.projectName.upper()}_H
        #define {self.projectName.upper()}_INCLUDE_{self.projectName.upper()}_H

        namespace my {{
            class A {{
            public:
            A();

            int p;
            }};
        }} // namespace my

        #endif // {self.projectName.upper()}_INCLUDE_{self.projectName.upper()}_H
        """

        #________________________________-src_file-________________________________#
        self.src_file_content: str = f"""
        #include "../include/{self.projectName}.h"

        namespace my {{
            A::A() : p(42) {{}}
        }} // namespace my
        """


        #________________________________-.git_ignore_content-________________________________#
        self.git_ignore_content: str = """
        build/
        compile_commands.json
        .clang-format
        .vscode
        .cache
        """

        #________________________________-.CMakeLists.txt__root-________________________________#
        self.Cmake_list_root: str = f"""
        cmake_minimum_required(VERSION 3.10)

        project("{self.projectName}")
        set(CMAKE_EXPORT_COMPILE_COMMANDS on)

        file(GLOB_RECURSE SRC_FILES "src/*.cpp")
        file(GLOB_RECURSE HDR_FILES "src/*.h")

        add_executable("{self.projectName}" main.cpp  ${{SRC_FILES}} ${{HDR_FILES}})

        set(CMAKE_CXX_STANDARD 20)
        set(CMAKE_CXX_STANDARD_REQUIRED ON)

        target_include_directories("{self.projectName}" PRIVATE ${{CMAKE_CURRENT_SOURCE_DIR}}/include)

        add_subdirectory(tests)

        target_compile_options("{self.projectName}" PRIVATE 
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

        target_link_options("{self.projectName}" PRIVATE 
            -fsanitize=address
            -fsanitize=undefined
        )

        target_compile_features("{self.projectName}" PRIVATE cxx_std_20)

        # If not Visual Studio generator, copy compile_commands.json
        if(NOT CMAKE_GENERATOR MATCHES "Visual Studio")
            add_custom_command(
                OUTPUT ${{CMAKE_CURRENT_SOURCE_DIR}}/compile_commands.json
                COMMAND ${{CMAKE_COMMAND}} -E copy ${{CMAKE_BINARY_DIR}}/compile_commands.json ${{CMAKE_CURRENT_SOURCE_DIR}}/compile_commands.json
                DEPENDS ${{CMAKE_BINARY_DIR}}/compile_commands.json
                COMMENT "Copying compile_commands.json..."
            )

            add_custom_target(copy_compile_commands ALL
                DEPENDS ${{CMAKE_CURRENT_SOURCE_DIR}}/compile_commands.json
            )
        endif()
        """

        #________________________________-.CMakeLists.txt__test-________________________________#
        self.Cmake_list_test_content: str = f"""
        cmake_minimum_required(VERSION 3.10)

        project({self.projectName}_test)

        find_package(GTest REQUIRED)

        include_directories(${{GTEST_INCLUDE_DIRS}})
        include_directories(${{CMAKE_SOURCE_DIR}}/include)  


        add_executable({self.projectName}_test {self.projectName}_test.cpp)

        target_include_directories({self.projectName}_test PRIVATE ${{CMAKE_SOURCE_DIR}}/include)
        target_link_libraries({self.projectName}_test ${{GTEST_LIBRARIES}} ${{GTEST_MAIN_LIBRARIES}} pthread)

        enable_testing()
        add_test(NAME {self.projectName}_test COMMAND {self.projectName}_test)
        target_compile_options({self.projectName}_test PRIVATE -Wall)
        """

        self.test_file_content: str = f"""
        #include <{self.projectName}.h>
        #include <gtest/gtest.h>

        TEST({self.projectName}Test, {self.projectName}Test__1) 
        {{}}

        int main(int argc, char** argv)
        {{
            ::testing::InitGoogleTest(&argc, argv);
            return RUN_ALL_TESTS();
        }}

        """

        #________________________________-.clang-format-________________________________#
        self.clang_format_conten: str = """
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
    print("Please enter project name:")
    project_name: str = input()

    project_content = ProjectContent(project_name)
    
    os.makedirs(project_name, exist_ok=True)

    write_file(os.path.join(project_name, "main.cpp"), project_content.main_cpp_content)
    write_file(os.path.join(project_name, ".clang-format"), project_content.clang_format_conten)
    write_file(os.path.join(project_name, ".gitignore"), project_content.git_ignore_content)
    write_file(os.path.join(project_name, "CMakeLists.txt"), project_content.Cmake_list_root)    
    
            
    os.makedirs(os.path.join(project_name, "build"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "src"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "include"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "tests"), exist_ok=True)
    
    write_file(os.path.join(project_name, "src",  f'{project_name}.cpp'), project_content.src_file_content)
    write_file(os.path.join(project_name, "include",  f'{project_name}.h'), project_content.header_file_content)
    
    write_file(os.path.join(project_name,  "tests", f'{project_name}_test.cpp'), project_content.test_file_content)
    write_file(os.path.join(project_name,  "tests", "CMakeLists.txt"), project_content.Cmake_list_test_content)
    
if __name__ == '__main__':
    main()