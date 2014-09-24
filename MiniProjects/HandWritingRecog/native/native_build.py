import os
import sys
from distutils.core import Extension, setup
os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.argv = [sys.argv[0], 'build_ext', '-i']
setup(ext_modules = [Extension('_hello', 
                               ["hello.c","DrawBlock.cpp"],
                               language = "c++",
)])
