#Below is a class representing a person. You'll see the
#Person class has three instance variables: name, age,
#and GTID. The constructor currently sets these values
#via a calls to the setters.
#
#Create a new function called same_person. same_person
#should take two instances of Person as arguments, and
#returns True if they are the same Person, False otherwise.
#Two instances of Person are considered to be the same if
#and only if they have the same GTID. It does not matter
#if their names or ages differ as long as they have the
#same GTID.
#
#You should not need to modify the Person class.

class Person:
    def __init__(self, name, age, GTID):
        self.set_name(name)
        self.set_age(age)
        self.set_GTID(GTID)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_GTID(self, GTID):
        self.GTID = GTID

    def get_name(self):
        return self.name

    def get_age(self):
       return self.age

    def get_GTID(self):
        return self.GTID

#Add your code below!
def same_person(person1,person2):
    if person1.get_GTID() == person2.get_GTID():
        return True
    else:
        return False
