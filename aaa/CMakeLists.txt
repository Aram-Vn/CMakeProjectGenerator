
cmake_minimum_required(VERSION 3.10)

project("aaa")

set(TARGET_NAME app_${PROJECT_NAME})
set(CMAKE_EXPORT_COMPILE_COMMANDS on)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

file(GLOB_RECURSE SOURCE_FILES 
    src/*.cpp
)

file(GLOB_RECURSE HEADER_FILES 
    include/*.h
)

add_executable(${TARGET_NAME} 
    main.cpp  
    ${SOURCE_FILES} 
    ${HEADER_FILES}
)

target_include_directories(${TARGET_NAME}
    PRIVATE 
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

include(CTest)
add_subdirectory(tests)
add_subdirectory(logger)

set(COMMON_COMPILE_OPTIONS
    -Wall
    -Wextra
    -Wshadow
    -Wswitch
    -pedantic
    -Wformat=2
    -Wnull-dereference
    -Wunused-parameter
    -Wunreachable-code
    -Wimplicit-fallthrough
)

set(COMMON_ERROR_OPTIONS
    -Werror
    -Werror=return-type
    -Werror=uninitialized
    -Werror=unused-result
    -Werror=strict-overflow
)

set(SANITIZER_FLAGS
    -fsanitize=undefined
    -fsanitize=address
    # -fsanitize=thread 
    -fsanitize=address
    -fno-omit-frame-pointer
)

target_compile_options(${TARGET_NAME} PRIVATE
    ${COMMON_COMPILE_OPTIONS}
    ${COMMON_ERROR_OPTIONS}
)

target_link_libraries(${TARGET_NAME} PRIVATE
    ${SANITIZER_FLAGS}
    one_header_logger
)

target_compile_definitions(one_header_logger INTERFACE
    LOG_LEVEL_THRESHOLD=LOG_LEVEL_DEBUG
    ENABLE_LOG_MUTEX
)

#-----------------------------------------------------------------------#
# if need to remove flags set lib as SYSTEM 
# to suppress warnings in external headers
#-----------------------------------------------------------------------#
# Remove -pedantic from the target’s options 
# get_target_property(target_options ${TARGET_NAME} COMPILE_OPTIONS)
# list(REMOVE_ITEM target_options "-pedantic")
# list(REMOVE_ITEM target_options "-Werror")
# set_property(TARGET ${TARGET_NAME} PROPERTY COMPILE_OPTIONS ${target_options})

# If not Visual Studio generator, copy compile_commands.json
if(NOT CMAKE_GENERATOR MATCHES "Visual Studio")
    add_custom_command(
        OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/compile_commands.json
        COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_BINARY_DIR}/compile_commands.json ${CMAKE_CURRENT_SOURCE_DIR}/compile_commands.json
        DEPENDS ${CMAKE_BINARY_DIR}/compile_commands.json
        COMMENT "Copying compile_commands.json..."
    )

    add_custom_target(copy_compile_commands ALL
        DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/compile_commands.json
    )
endif()
        