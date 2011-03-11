#!/usr/bin/env python
# For some reason, building exes with py2exe doesnt work right now.
from distutils.core import setup
import sys, os, shutil, sys

scripts=['digenpy', 'digenpy-gtk']
if os.name is not "posix":
    if os.name is "nt":
        import py2exe
    shutil.copyfile('digenpy','digenpy.py')
    shutil.copyfile('digenpy-gtk','digenpy-gtk.py')
    scripts=['digenpy.py', 'digenpy-gtk.py']

opts = {
    "py2exe": {
        'includes': 'cairo, pango, pangocairo, atk, gobject, gio',
        "excludes": "atk,gdk",
        "dll_excludes": [
        "iconv.dll","intl.dll","libatk-1.0-0.dll",
        "libgdk_pixbuf-2.0-0.dll","libgdk-win32-2.0-0.dll",
        "libglib-2.0-0.dll","libgmodule-2.0-0.dll",
        "libgtk-win32-2.0-0.dll","libpango-1.0-0.dll",
        "libpangowin32-1.0-0.dll"],
        'packages': ['Digenpy_'],
        }
    }

setup(name='Digenpy',
      version='1.1',
      description='Python default wireless dictionary generators',
      author='David Francos Cuartero (XayOn)',
      windows = [{"script": "digenpy-gtk.py" }],
      console = [{"script": "digenpy.py" }],
      author_email='xayon@davidfrancos.net',
      url='http://github.com/XayOn/Digenpy',
      packages=['Digenpy_'],
      scripts=scripts,
      options=opts,
      data_files=[(sys.prefix + '/share', ['digenpy.ui'])],
     )
