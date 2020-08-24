""" Module to Check or Print the Builtin Module's Names in Python """

# pylint: disable = E1133
# E1133: Non-iterable value is used in an iterating context (not-an-iterable)

import sys
import pkgutil
import pkg_resources

def builtins():
    """ Return the set of Builtin Module Names in Local Python. No Input. """
    exclude = {module.project_name for module in pkg_resources.working_set}
    return {mod.name for mod in pkgutil.iter_modules() if mod.name not in exclude}|set(sys.modules)

def print_builtins():
    """ Prints the list of built-in module name, 1 per line. No Input. No Return Values. """
    for serial, name in enumerate(sorted(builtins())):
        print(f"{serial+1}. {name}")

def check_builtins(key):
    """
    Checks Whether Given Module Name is a Builtin Module in Present Python.
    Input: Module Name.
    Output: Returns True if found and False if not.
    """
    return str(key) in builtins()

def main():
    """ Main Function of py_builtins Module """

    if len(sys.argv) > 1:
        # Checks if Command Line Argument has Module Name. If yes, checks whether Built-in.
        for module in sys.argv[1:]:
            print(f">> \x1B[3m{module}\x1B[23m is "
                  f"{'a Built-in' if check_builtins(module) else 'Not a Built-in'}"
                  f" Module in Python {sys.version[:sys.version.index('(') - 1]}.")
    else:
        # Printing list of builtins
        print_builtins()

if __name__ == '__main__':
    main()
