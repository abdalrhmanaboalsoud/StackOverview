
# Object-Oriented Programming (OOP) Overview

## Table of Contents
1. [Introduction](#introduction)
2. [Core Concepts of OOP](#core-concepts-of-oop)
   - [Classes and Objects](#classes-and-objects)
   - [Encapsulation](#encapsulation)
   - [Abstraction](#abstraction)
   - [Inheritance](#inheritance)
   - [Polymorphism](#polymorphism)
3. [Advanced OOP Concepts](#advanced-oop-concepts)
   - [Composition](#composition)
   - [Aggregation](#aggregation)
   - [Method Overriding](#method-overriding)
   - [Method Overloading](#method-overloading)
   - [Abstract Classes](#abstract-classes)
   - [Interfaces](#interfaces)
4. [Benefits of OOP](#benefits-of-oop)
5. [Conclusion](#conclusion)
6. [References](#references)

## Introduction
Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to represent data and methods. OOP allows developers to create modular programs that are easier to manage and scale.

## Core Concepts of OOP

### Classes and Objects
- **Classes:** A blueprint for creating objects. A class encapsulates data for the object and methods to manipulate that data.
- **Objects:** Instances of classes. Each object has its own properties and behaviors defined by its class.
- **Example:**
    ```
    class Dog:
        def __init__(self, name, breed):
            self.name = name
            self.breed = breed
        
        def bark(self):
            return f"{self.name} says woof!"
    
    my_dog = Dog("Buddy", "Golden Retriever")
    print(my_dog.bark())  # Output: Buddy says woof!
    ```

### Encapsulation
- **Definition:** The bundling of data (attributes) and methods (functions) that operate on that data within one unit (class), restricting access to some of the object's components.
- **Example:**
    ```
    class BankAccount:
        def __init__(self, balance=0):
            self.__balance = balance  # Private attribute
        
        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount

        def get_balance(self):
            return self.__balance
    
    account = BankAccount()
    account.deposit(100)
    print(account.get_balance())  # Output: 100
    ```

### Abstraction
- **Definition:** The concept of hiding complex reality while exposing only the necessary parts. It helps to reduce programming complexity and increase efficiency.
- **Example:**
    ```
    from abc import ABC, abstractmethod

    class Animal(ABC):
        @abstractmethod
        def sound(self):
            pass

    class Cat(Animal):
        def sound(self):
            return "Meow"

    class Dog(Animal):
        def sound(self):
            return "Woof"

    my_cat = Cat()
    my_dog = Dog()
    print(my_cat.sound())  # Output: Meow
    print(my_dog.sound())  # Output: Woof
    ```

### Inheritance
- **Definition:** A mechanism where a new class (child class) inherits attributes and methods from an existing class (parent class), promoting code reuse.
- **Example:**
    ```
    class Animal:
        def speak(self):
            return "Animal speaks"

    class Cat(Animal):
        def speak(self):
            return "Meow"

    class Dog(Animal):
        def speak(self):
            return "Woof"

    cat = Cat()
    dog = Dog()
    print(cat.speak())  # Output: Meow
    print(dog.speak())  # Output: Woof
    ```

### Polymorphism
- **Definition:** The ability to present the same interface for different underlying data types. It allows methods to do different things based on the object it is acting upon.
- **Example:**
    ```
    def animal_sound(animal):
        print(animal.speak())

    animal_sound(cat)  # Output: Meow
    animal_sound(dog)  # Output: Woof
    ```

## Advanced OOP Concepts

### Composition
- **Definition:** A design principle in which a class is composed of one or more objects from other classes. It establishes a "has-a" relationship.
- **Example:**
    ```
    class Engine:
        def start(self):
            return "Engine started"

    class Car:
        def __init__(self):
            self.engine = Engine()  # Car "has-a" Engine

        def start(self):
            return self.engine.start()

    my_car = Car()
    print(my_car.start())  # Output: Engine started
    ```

### Aggregation
- **Definition:** A special form of association where a class contains references to objects of another class, establishing a "whole-part" relationship. Unlike composition, aggregation does not imply ownership.
- **Example:**
    ```
    class Department:
        def __init__(self, name):
            self.name = name

    class University:
        def __init__(self):
            self.departments = []  # University "has-a" list of Departments

        def add_department(self, department):
            self.departments.append(department)

    cs_department = Department("Computer Science")
    university = University()
    university.add_department(cs_department)
    print(university.departments[0].name)  # Output: Computer Science
    ```

### Method Overriding
- **Definition:** The ability of a subclass to provide a specific implementation of a method that is already defined in its superclass.
- **Example:**
    ```
    class Parent:
        def show(self):
            return "Parent's show method"

    class Child(Parent):
        def show(self):
            return "Child's show method"

    child = Child()
    print(child.show())  # Output: Child's show method
    ```

### Method Overloading
- **Definition:** A feature that allows a class to have more than one method with the same name but different parameters. This is not natively supported in Python but can be achieved using default arguments.
- **Example:**
    ```
    class Math:
        def add(self, a, b, c=0):
            return a + b + c

    math = Math()
    print(math.add(1, 2))      # Output: 3
    print(math.add(1, 2, 3))   # Output: 6
    ```

### Abstract Classes
- **Definition:** A class that cannot be instantiated and is designed to be a base class. It can contain abstract methods that must be implemented by derived classes.
- **Example:**
    ```
    from abc import ABC, abstractmethod

    class Vehicle(ABC):
        @abstractmethod
        def start_engine(self):
            pass

    class Motorcycle(Vehicle):
        def start_engine(self):
            return "Motorcycle engine started"

    bike = Motorcycle()
    print(bike.start_engine())  # Output: Motorcycle engine started
    ```

### Interfaces
- **Definition:** A contract that a class must follow, defining methods that must be created within any class that implements the interface.
- **Example:**
    ```
    from abc import ABC, abstractmethod

    class Vehicle(ABC):
        @abstractmethod
        def start_engine(self):
            pass

        @abstractmethod
        def stop_engine(self):
            pass

    class Car(Vehicle):
        def start_engine(self):
            return "Car engine started"

        def stop_engine(self):
            return "Car engine stopped"

    my_car = Car()
    print(my_car.start_engine())  # Output: Car engine started
    print(my_car.stop_engine())   # Output: Car engine stopped
    ```

## Benefits of OOP
1. **Modularity:** OOP allows for the modular organization of code. Each class can be developed and tested independently.
2. **Reusability:** Classes can be reused in different programs, reducing redundancy and improving efficiency.
3. **Maintainability:** Code is easier to maintain and modify due to encapsulation and clear class definitions.
4. **Flexibility:** OOP promotes flexibility through polymorphism and inheritance, allowing for changes in implementations without affecting other parts of the code.

## Conclusion
Object-Oriented Programming is a powerful paradigm that facilitates better organization, reusability, and maintenance of code. Understanding OOP principles is crucial for developing efficient software systems.

## References
- [Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [OOP Concepts Explained with Real-World Examples](https://www.tutorialspoint.com/python/python_classes_objects.htm)
