#!/usr/bin/env python
import os 
from distutils.core import setup
from distutils.extension import Extension
os.environ["CC"] = "g++"
os.environ["CXX"] = "g++" 
setup(name="PackageName",
    ext_modules=[
        Extension("hello", ["hellomodule.cpp"],
        libraries = ["boost_python"])
    ])
