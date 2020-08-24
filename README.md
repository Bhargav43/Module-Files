# Module-Files
Finds the Modules Files (The initial loading file when imported) for Built-in and PIP installed modules.

<div class="text-red mb-2">
  .text-red
</div>

##### _Note: This might not be 100% accurate as the packages pkg_resources.py and pkgutil.py fails to give the accurate results in certain environment._

## Base System's Configurations :wrench:
**Sno.** | **Name** | **Version/Config.**
-------: | :------: | :------------------
1 | Operating System | Windows 10 x64 bit
2 | Python | Version 3.7.8rc1 x64 bit
3 | IDE | VS Code 1.48.1 x64 bit

## 1. py_builtins
This check whether the given module name is a Built-in Module. This can be used from command line as well as from function calls. Following are the types of calls.
#### From Command-line:
```
:: Printing List of Built-ins
python py_builtins.py

:: Checking for a Module Name (eg. Pandas)
python py_builtins.py pandas
>> pandas is Not a Built-in Module in Python 3.7.8rc1.

:: Checking with Multiple Module Names
python py_builtins.py os sys pandas
>> os is a Built-in Module in Python 3.7.8rc1.
>> sys is a Built-in Module in Python 3.7.8rc1.
>> pandas is Not a Built-in Module in Python 3.7.8rc1.
```

#### From Function Calls:
```python
from py_builtins import print_builtins, check_builtins

# Printing List of Built-ins
print_builtins()

# Checking for a Module Name (eg. Pandas)
check_builtins('pandas')
```

## 2. module_files
This check for the module file (The initial loading file when imported) for Built-in and PIP installed modules. Also, whether that can be imported separately other than from program. This can be used from command line as well as from function calls. Following are the types of calls.
#### From Command-line:
```
:: Selective Names
python module_file.py sys os pandas venv

:: Builtins
python module_file.py /B

:: PIP Installed
python module_file.py /I

:: All Modules
python module_file.py
(or)
python module_file.py /A
```

#### From Function Calls:
```python
from module_files import file_path, builtins, installed

# Selective Names
[file_path(module) for module in ('sys', 'os', 'pandas', 'venv')]

# Builtins
[file_path(name) for name in builtins()]

# PIP Installed
[file_path(name) for name in installed()]

# All Modules
[file_path(name) for name in builtins()|installed()]
```
