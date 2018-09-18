Sample Project
==============

Description
-----------

I often find myself working on self-contained projects involving the 
manipulation and analysis of substantial quatities of data in various 
proprietary formats. Generally I start on these by working with the data by 
hand and creating command line tools for tasks I find myself repeating.
Usually, as soon as I've written two or three small tools, I start 
refactoring some of the code into modules. Before long, I find the need to 
have different configurations for different systems or data sets, so I add 
support for configuration files. And so on. Before long I can have a full 
suite of command line tools, maybe a GUI or web interface, all sharing custom
modules and configuration options. I prefer to keep these neatly 
self-contained under a single directory whose installation on a new machine
is as simple as cloning a git repository and installing 3rd party
requirements. 

This sample Python project illustrates some project level idioms I like to 
use in these cases. It is intended to be suitable to use as a skeleton for 
new projects. 


Directory Structure
-------------------

I work on Unix/Linux systems so I'm accustomed to the Filesystem
Hierarchy Standard (FHS) and I base my project directory structure on it.

    sample/
         |-- bin/
         |   |-- _project.py
         |   '-- sample.py
         |-- doc/
         |   |-- LICENSE
         |   '-- TODO
         |-- etc/
         |   '-- sample.ini
         |-- lib/
         |   '-- samplelib.py
         |-- var/
         |   |-- log/      
         |   '-- run/      
         |       '-- sample/      
         |           '---- sample.db      
         |-- .gitignore 
         '-- README.md 

Files
-----

The files in this sample are only meant to represent some of the types of 
files a typical project might include. One exception is the `project.py` file
in the `bin/` directory. In order to use the lib directory, I add boilerplate
to my tools that adds the lib directory to `sys.path`. This boilerplate code
goes into the `_project.py` file and then I just need to `import _project` in
each of my tools. This is also a handy place to add other code which I need 
in every tool, e.g. code to read a configuration file. 
