import os
from ctypes import cdll

# Set full path to the required DLLs
libzbar_path = r'C:\path\to\libzbar-64.dll'
libiconv_path = r'C:\path\to\libiconv.dll'

# Load the DLLs explicitly
cdll.LoadLibrary(libzbar_path)
cdll.LoadLibrary(libiconv_path)

from pyzbar.pyzbar import decode
