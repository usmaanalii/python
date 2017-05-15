# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


# Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name


# Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name


# Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


# Employee is-a object
class Employee(Person):

    def __init__(self, name, salary):
        # Employee has-a name
        super(Employee, self).__init__(name)
        # Employee has a salary
        self.salary = salary


# Fish is-a object
class Fish(object):
    pass


# Salmon is-a fish
class Salmon(Fish):
    pass


# Halibut is-a fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a cat
satan = Cat("Satan")

# mary is-a person
mary = Person("Mary")

# frank is-a employee
frank = Employee("Frank", 120000)

# rover is-a pet of franks
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# crouse is-a salmon
crouse = Salmon()

# harry is-a halibut
harry = Halibut()
