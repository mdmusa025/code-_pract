# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

#     def display(self):
#         print(f"Name: {self.name}, Roll: {self.roll}")

# # Object creation
# s1 = Student("Musa", 101)
# s1.display()


# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# def make_sound(animal):
#     animal.sound()

# d = Dog()
# c = Cat()

# make_sound(d)  # Output: Bark
# make_sound(c)  # Output: Meow

# number=[5,2,3,1]
# number.sort()
# print(number)

# even_list=[x for x in range (1,20)if x%2!=0]
# print(even_list)

# even_list=[x for x in range (1,20)if x%2==0]
# print(even_list)


# fruit=["apple","ball","cherry","mango"]
# new_list=[]
# for x in fruit:
#     if "e" in x:
#         new_list.append(x)
# print(new_list)

# words = ["apple", "banana", "cherry"]
# lower_words = [word.lower() for word in words]
# print(lower_words)  

# fruits = ["mango", "orange", "grape"]
# first_letters = [fruit[0] for fruit in fruits]
# print(first_letters)  # Output: ['m', 'o', 'g']


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# my_tuple = ("apple", "banana", "cherry")
# print(my_tuple)
# # Output: ('apple', 'banana', 'cherry')

# my_tuple = ('apple', 'banana', 'cherry', 'banana')


# print(my_tuple.index('banana'))

# my_set={1,2,3,4,5}
# another_set=set([1,2,3,4])
# print(another_set)


# my_set.add(6)

# my_set.remove(3)    
# my_set.discard(4)    


# my_set.clear()


# print(2 in my_set) 
# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# fruits.remove("banana")
# print(fruits)  # Output: {'apple', 'cherry', 'orange'}

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):  
#         print("Dog barks")


# a = Animal()
# d = Dog()

# a.speak()  
# d.speak()  


# class student:
#     def speak(self):
#         print("hindi")

# class amar(student):
#     def speak(self):  
#         print("kannada")

# a=student()
# d=amar()

# a.speak()
# d.speak()
 
# class BankAccount:
#     def interest_rate(self):
#         print("Base interest rate is 3%")

# class SavingsAccount(BankAccount):
#     def interest_rate(self):
#         print("Savings interest rate is 5%")

# class FixedDeposit(BankAccount):
#     def interest_rate(self):
#         print("Fixed deposit interest rate is 7%")

# class bussinessAccount(BankAccount):
#     def interest_rate(self):
#         print("business interest rate is 10%")

# class currentsaving(BankAccount):
#       def interest_rate(self):
#         print("current interest rate is 10%")


# s = SavingsAccount()
# f = FixedDeposit()
# b = bussinessAccount()
# c= currentsaving()

# s.interest_rate()  
# f.interest_rate()
# b.interest_rate()
# c.interest_rate()

# class Flyable:
#     def fly(self):
#         print("Can fly")

# class Swimmable:
#     def swim(self):
#         print("Can swim")

# class Duck(Flyable, Swimmable):  # Inheriting from two classes
#     def quack(self):
#         print("Duck quacks")

# duck = Duck()
# duck.fly()
# duck.swim()
# duck.quack()

# class Flyable:
#     def fly(self):
#         print("Can fly")

# class Swimmable:
#     def swim(self):
#         print("Can swim")

# class Duck(Flyable, Swimmable):  # Inheriting from two classes
#     def quack(self):
#         print("Duck quacks")

# duck = Duck()
# duck.fly()
# duck.swim()
# duck.quack()

# class Grandparent:
#     def home(self):
#         print("Grandparent's home")

# class Parent(Grandparent):
#     def car(self):
#         print("Parent's car")

# class Child(Parent):
#     def bike(self):
#         print("Child's bike")



# child = Child()
# child.home()
# child.car()
# child.bike()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year":2020
  
}
print(thisdict)

thisdict = {
  "brand": "bmw",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict={
    "brand":"indica",
    "model":"old",
    "year": 2273,
    "year": 3030
} 
print(thisdict["model"])







