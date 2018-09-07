"""Classes & Objects
A little bit of theory:
Objects are a representation of real world objects like cars, dogs, or bikes. The objects share two main characteristics: data and behavior.

Cars have data, like number of wheels, number of doors, and seating capacity They also exhibit behavior: they can accelerate, stop, show how much fuel is left, and so many other things.

We identify data as attributes and behavior as methods in object-oriented programming. Again:

Data → Attributes and Behavior → Methods

And a Class is the blueprint from which individual objects are created. In the real world, we often find many objects with the same type. Like cars. All the same make and model (and all have an engine, wheels, doors, and so on). Each car was built from the same set of blueprints and has the same components.
"""

"""Python, as an Object-Oriented programming language, has these concepts: class and object.

A class is a blueprint, a model for its objects.

So again, a class it is just a model, or a way to define attributes and behavior (as we talked about in the theory section). As an example, a vehicle class has its own attributes that define what objects are vehicles. The number of wheels, type of tank, seating capacity, and maximum velocity are all attributes of a vehicle.

With this in mind, let’s look at Python syntax for classes:
"""

#class vehicle example1

class vehicle_example1:
    pass #The pass statement is a null operation; nothing happens when it executes.

car = vehicle_example1()
print(car)

#class vehicle example2

"""We use the init method. We call it a constructor method. So when we create the vehicle object, we can define these attributes.
"""

class vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    
    def make_noise(self):
        print('VRUUUUUUUM')

"""
Imagine that we love the Tesla Model S, and we want to create this kind of object. It has four wheels, runs on electric energy, has space for five seats, and the maximum velocity is 250km/hour (155 mph). 
"""

#tesla_model_s = Vehicle(4, 'electric', 5, 250)

"""
All attributes are set. But how can we access these attributes’ values? We send a message to the object asking about them. We call it a method. It’s the object’s behavior. 
"""

def number_of_wheels(self):
        return self.number_of_wheels

def set_number_of_wheels(self, number):
        self.number_of_wheels = number

"""
This is an implementation of two methods: number_of_wheels and set_number_of_wheels. We call it getter & setter. Because the first gets the attribute value, and the second sets a new value for the attribute.
And we can use these methods as attributes:
"""

tesla_model_s = vehicle(4, 'electric', 5, 250)
print(tesla_model_s.number_of_wheels) # 4
tesla_model_s.number_of_wheels = 2 # setting number of wheels to 2
print(tesla_model_s.number_of_wheels) # 2

tesla_model_s = vehicle(4, 'electric', 5, 250)
tesla_model_s.make_noise()