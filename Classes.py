# Classes are extremely important in programmaing and they are not specific to Python.
# We use classes to define new types. For example, the basic types we learnt like numbers, boolean, strings
# We also learnt complex types like lists, dictionaries etc. These types are okay, but not sufficient to model more complex concepts. 
# So we have CLASSES, that we can use to define new types to model real concepts.
# Let us see below, how to define a new type - Point, and this will be used for working with points

# We define a class below, we use class keyword for this. Point is the name of the class.
# Pascal naming convention is followed here. i.e. First letter capital it could have been, PointObjectType, OrangeVariation, ShoppingCart, EmailClient
# When naming variables and function, we used small case seperated by underscore, but this is class and therefore different, and should be named as below

class Point:                # Colon means, that a block follows. In this block, we can define all functions and methods that belong to point.
    def move(self):         # This is an example of method that can be used with the object can be called using dot operator
        print("Move")


    def draw(self):         # This is another example of method that can be called using dot operator
        print("Draw")


# So above, we defined a new type with the use of class. With this new type, we can create a new objects.
# An object is an instance of a class. A class simply defines a blueprint or the template for creating object.
# The object is the actual instance based on that class' blueprint. And there can be 10s or 100s of objects/instances on the screen related to a class.
# To create an object, we type the name of the class and call it like a function, and this creates a new object and returns it.
# And we can store an object in a variable

point1 = Point()        # Point() here is an object/instance and point1 the variable in which we are storing it
point1.draw()           # Like we did is lists, functions, strings etc. we can use dot operator to call methods .draw() is method

# Apart from methods, these objects can also have attributes. And these attributes are like variables that belong to a particular object
# Like below you can see these attributes .x and .y, belonging to point1 object. And these attributes belong to only point1 object and not to point2 object. 
# Therefore, when you try to print point2.x, it gives an attribute error. It shows each object is a different instance of a point class.


point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
print(point2.x)

