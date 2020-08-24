""" Module to Search the Builtin & PIP Installed Module's Load-File on Disk """

# pylint: disable = W0106, W0703, E0704, E1133
# W0106: Expression is assigned to nothing (expression-not-assigned)
# W0703: Catching too general exception Exception (broad-except)
# E0704: The raise statement is not inside an except clause (misplaced-bare-raise)
# E1133: Non-iterable value is used in an iterating context (not-an-iterable)

import sys
import pkgutil
import importlib
import pkg_resources

def file_path(module):
    """
    Searches Location of Module's Load File
    Input: Module Name (String)
    Output: Path if found, else None
    """
    version = sys.version[:sys.version.index('(') - 1]
    try:
        path = importlib.util.find_spec(module).origin
        if path is None:
            raise
        print(f"The Module \x1B[3m{module}\x1B[23m in Python {version} is at: {path}")
        return {'name': module, 'path': path}
    except Exception:
        if module in builtins():
            print(f"CannotImportError: Module \x1B[3m{module}\x1B[23m"
                  f" in Python {version} not accessible.")
        else:
            print(f"NotFoundError: No Module \x1B[3m{module}\x1B[23m found in Python {version}.")
        return None

def builtins():
    """ Return the set of Builtin Module Names in Local Python. No Input. """
    exclude = {module.project_name for module in pkg_resources.working_set}
    return {mod.name for mod in pkgutil.iter_modules() if mod.name not in exclude}|set(sys.modules)

def installed():
    """ Return the set of PIP Installed Module Names in Local Python. No Input. """
    try:
        collection = {module.project_name for module in pkg_resources.working_set}
        return collection
    except Exception as desc:
        print(f"Failed with reason as {desc}")
        return None

def main():
    """ Main Function for module_file """
    if len(sys.argv) > 1:
        if sys.argv[1] == '/B':
            # Built-ins
            [file_path(name) for name in builtins()]
        elif sys.argv[1] == '/I':
            # PIP Installed
            [file_path(name) for name in installed()]
        elif sys.argv[1] == '/A':
            # All Modules
            [file_path(name) for name in builtins()|installed()]
        else:
            # Selective Names
            [file_path(module) for module in sys.argv[1:]]
    else:
        # All Modules (Again)
        [file_path(name) for name in builtins()|installed()]

if __name__ == "__main__":
    main()
