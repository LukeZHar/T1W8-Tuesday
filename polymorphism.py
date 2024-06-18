class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
# Function to make any animal speak
def animal_sound(animal):
    print(animal.speak())

# Creating instance of Dog and Cat
dog = Dog()
cat = Cat()

# Using polymorphism to call the speak method
animal_sound(dog)
animal_sound(cat)