# Packages are basically another way to organize our code.
# A real project may contain 100 or thousands of files/modules.
# You would not want to add al of them in the directory as it would be bloated with files/modules
# So a better approach is to organise all related modules into a package. So package is a container for modules
# So package is a directory or a folder in filesystem terms
# So package is like a Men's section in a mart and modules are like different sections in that - Shoes, Jeans etc.
# Similarly, you may have other packages analogous women's, kids etc. with their seperate sections
# To create a package, we need to create a folder and to this folder we need to add __init__.py file
# Python will recognise the directory as a package because of the the added file type.
# We created ShoppingCart package, we use following syntax for importing modules and functions

# import package.modulename               
import ecommerce.shipping                                       # We imported package using path package.modulename
ecommerce.shipping.calc_shipping()                              # To use function present in module, we would use complete path followed by methodname i.e calc_shipping()

# from package.modulename import function/method/class etc.
from ecommerce.shipping import calc_shipping                    # We are importing specific method using from package.modulename import methodname i.e. calc_shipping()
calc_shipping()

# from package import modulename
from ecommerce import shipping                                  # We are importing shipping module using from package import modulename i.e shipping
shipping.calc_shipping()                                        # So we will need to use modulename.methodname()