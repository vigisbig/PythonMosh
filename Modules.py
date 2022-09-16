# Modules in Python is basically a file with some Python code.
# We use modules to organize our code into multiple files, just like sections
# in supermarket. This let's use structure the code properly and also give ability to reuse it.
# In a particular module, you would want to put all related functions and classes.
# And we will be able to import that module into any program where we need and use it.
# There are many existing modules that are present and we can install them, import them and use them.
# There are also many pre-installed modules in Python that we can use like random,email etc. We can find them by searching -Python builtin modules in google

# When naming your python file.....make sure that it's not same as a module name.

# Difference between module and package

# A module is a file containing Python code. A package, however, is like a directory that holds sub-packages and modules.
# A package must hold the file __init__.py. This does not apply to modules.

import convertors                   # Asking to import convertors, it is a file with two functions that we want

print(convertors.kg_to_lbs(130))    # calling the kg_to_lbs method using dot operator and using it, printing output. 
