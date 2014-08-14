#C:\Users\didutta\workspace\FibNative>C:\DDDD\android-ndk-r10\ndk-build APP_ABI=all
LOCAL_PATH := $(call my-dir)
 
include $(CLEAR_VARS)
 
# Here we give our module name and source file(s)
LOCAL_MODULE    := com_example_fibnative_FibLib
LOCAL_SRC_FILES := com_example_fibnative_FibLib.cpp
LOCAL_LDLIBS += -llog
include $(BUILD_SHARED_LIBRARY)