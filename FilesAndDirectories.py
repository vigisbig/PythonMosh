# pathlib is a module in default library. It provides classes that we can use to create objects to work with directories and files
# from pathlib import Path              This is used to import main class Path, from pathlib module. P is capital i.e. Path is a class

from pathlib import Path

# We can either use
# Absolute path or
# Relative path - We are using relative path here.

path = Path()                           # Creating new object with class Path. Having no argument for Path() means current directory
print(path.exists())                    # Checking if path that we provided exists or not. .exists is the method that we use for this with the newly created object
path = Path("ecommerce")                # Changing object and providing an argument for the Path() to see if the directory by name ecommerce exists
print(path.exists())                    
path = Path("email")                    # Changing object and providing an argument for the Path() to see if the directory by name email exists
print(path.exists())                    
#path.rmdir()                            # This can be used to remove directory, .mkdir() method can be used to create a directory

path = Path()                           # Changed path to current directory
print(path.glob('*.py'))                # Calling glob method, with this we can search for files and directories in the current path. Using '*.*' will give us all files. 
                                        # We can also search for '*.py', '*.xls'. Printing this gives a generator object
#for file in path.glob('*.py'):         # Instead, using a for loop to iterate, and this will print names of all python files present in the current directory
#   print(file)
for dir in path.glob('*'):              # This will print all files as well as directories in the current path
    print(dir)