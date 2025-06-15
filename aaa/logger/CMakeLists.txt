
cmake_minimum_required(VERSION 3.14)
project(one_header_logger LANGUAGES CXX)

add_library(one_header_logger INTERFACE)

target_include_directories(one_header_logger INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})

# Allow user to define logging threshold and mutex at compile time
target_compile_definitions(one_header_logger INTERFACE
    $<$<BOOL:${LOG_LEVEL_THRESHOLD}>:LOG_LEVEL_THRESHOLD=${LOG_LEVEL_THRESHOLD}>
    $<$<BOOL:${ENABLE_LOG_MUTEX}>:ENABLE_LOG_MUTEX>
)

# default threshold if none is set
if(NOT DEFINED LOG_LEVEL_THRESHOLD)
    target_compile_definitions(one_header_logger INTERFACE LOG_LEVEL_THRESHOLD=LOG_LEVEL_DEBUG)
endif()
        