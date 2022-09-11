# Python comes with standard library that contains several modules for common tasks like sending email
# working with date and time, generating random values and passwords etc. So there's a lot of functionality 
# that you can use and you don't need to code that from scratch. To find this standard library search google
# python 3 module index and it would be the first result.

import random           #   Since random is a built in module, you don't need to have a file random.py, and Python knows where to find it
for i in range(3):
    print(random.random())
