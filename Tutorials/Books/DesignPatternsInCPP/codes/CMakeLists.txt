cmake_minimum_required(VERSION 2.8.4)
project(codes)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

#set(SOURCE_FILES main.cpp)
set(SOURCE_FILES builder1.cpp)
add_executable(codes ${SOURCE_FILES})