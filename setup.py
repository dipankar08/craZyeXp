#!/usr/bin/env python
import os
from setuptools import setup
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "quickSms",
    version = "1.0",
    author = "Dipankar Dutta",
    author_email = "dutta.dipankar08@gmail.com",
    description = ("Easy way to send an sms from CLI using 160by2/way2sms"),
    license = "BSD",
    keywords = "sms 160by2 way2sms message chat mobile",
    url = "http://github.com/dipankar08/craZyeXp/",
    packages=['smsEngine'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
