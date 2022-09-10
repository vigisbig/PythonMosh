class Point:                    # Constructors are used for instantiating an object. The task of constructors is to initialize(assign values) 
    def __init__(self,x,y):     # to the data members of the class when an object of the class is created. 
        self.x = x              # In Python the __init__() method is called the constructor and is always called when an object is created. 
        self.y = y              # Self here is a reference to the current object. The method is called constructor since 
                                # it is used to create object. The x,y are the parameters here. The object will be defined 
                                # based on the argument values used while defining that particular object.                            
    def move(self):
        print("move")

    
    def draw(self):
        print("draw")


# A constructor is a function that gets called at the time of creating an object
# Below you can see the attributes 10,20 and these are the values that will be 
# initialised for the object point below. And this is done by defining a special method called constructor in the class above

point1 = Point(10,20)       # point1 object created, and initialized values 10 and 20 for x and y respectively.
point2 = Point(20,20)

print(point1.x)
point1.x = 12               # We can also change the value of the object if needed using this syntax.
print(point1.x)


