
cmake_minimum_required(VERSION 3.10)

project(aaa_test)

find_package(GTest QUIET)

if(NOT GTest_FOUND)
    message(STATUS "[...] GTest not found. Attempting to install using package manager...")
    if(UNIX AND NOT APPLE)
        execute_process(
            COMMAND sh -c "sudo apt-get install -y libgtest-dev || sudo dnf install -y gtest-devel || 
                           sudo pacman -S --noconfirm gtest || yay -S --noconfirm gtest"
            RESULT_VARIABLE PACKAGE_INSTALL_RESULT
            OUTPUT_VARIABLE PACKAGE_INSTALL_OUTPUT
            ERROR_VARIABLE PACKAGE_INSTALL_ERROR
        )
    elseif(APPLE)
        execute_process(
            COMMAND brew install googletest
            RESULT_VARIABLE PACKAGE_INSTALL_RESULT
            OUTPUT_VARIABLE PACKAGE_INSTALL_OUTPUT
            ERROR_VARIABLE PACKAGE_INSTALL_ERROR
        )
    elseif(WIN32)
        execute_process(
            COMMAND powershell -Command "scoop install gtest"
            RESULT_VARIABLE PACKAGE_INSTALL_RESULT
            OUTPUT_VARIABLE PACKAGE_INSTALL_OUTPUT
            ERROR_VARIABLE PACKAGE_INSTALL_ERROR
        )
    else()
        set(PACKAGE_INSTALL_RESULT -1)
    endif()

    if(PACKAGE_INSTALL_RESULT EQUAL 0) 
        find_package(GTest QUIET)

        if(GTest_FOUND)
            message(STATUS "[ V ] Successfully installed GTest using the package manager.")
        else()
            message(WARNING "[ X ] Installation via package manager was successful, but GTest could not be found.")
        endif()
    else()
        message(WARNING "[ X ] Failed to install GTest using the package manager.")
        message(STATUS "[ X ] Package manager output: ${PACKAGE_INSTALL_OUTPUT}")
        message(STATUS "[ X ] Package manager error: ${PACKAGE_INSTALL_ERROR}")
    endif()
endif()

include_directories(${GTEST_INCLUDE_DIRS})
include_directories(${CMAKE_SOURCE_DIR}/include)  

file(GLOB_RECURSE SRC_FILES "${CMAKE_SOURCE_DIR}/src/*.cpp")
file(GLOB_RECURSE HDR_FILES "${CMAKE_SOURCE_DIR}/include/*.h")

add_executable(aaa_test aaa_test.cpp)

target_include_directories(aaa_test PRIVATE ${CMAKE_SOURCE_DIR}/include)
target_link_libraries(aaa_test ${GTEST_LIBRARIES} ${GTEST_MAIN_LIBRARIES} pthread)

enable_testing()
add_test(NAME aaa_test COMMAND aaa_test)
target_compile_options(aaa_test PRIVATE -Wall)
        