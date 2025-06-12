class Student:
    
    # The init function is called automatically everytime a class is used to create an object
    # I initilize this init function to take in a first name, last name, age, and id
    # and then assign the given values to the object as its properties
    def __init__(self, fname, lname, age, id):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.id = id
        
    # The str function is essentially the toString and displays how the object will look
    # when it is called in a print statement. Otherwise, it will return a default object string
    def __str__(self):
        return f"Name: {self.fname} {self.lname}\nAge: {self.age}\nID: {self.id}\n"
    
    # the parameter self references the current instance of the class and can be used
    # to access the variables of the class