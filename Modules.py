# Modules in Python is basically a file with some Python code.
# We use modules to organize our code into multiple files, just like sections
# in supermarket. This let's use structure the code properly and also give ability to reuse it.
# In a particular module, you would want to put all related functions and classes.
# And we will be able to import that module into any program where we need and use it.

import convertors                   # Asking to import convertors, it is a file with two functions that we want

print(convertors.kg_to_lbs(130))    # calling the kg_to_lbs method using dot operator and using it, printing output. 
