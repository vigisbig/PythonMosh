# We can also import selective functions too, and this would enable us to write code as if the
# functions are present in this program itself, look at the code below and compare it to the
# one we wrote in Modules.py

import convertors
from convertors import kg_to_lbs

print(kg_to_lbs(130))
print(convertors.kg_to_lbs(130)) # This will till work as it did in Modules, but you can also use
                                 # the code as above since we imported that function.