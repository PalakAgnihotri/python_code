# 1 Write a program illustrating class definition and accessing class members. 

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.is_started = True

#     def start_engine(self):
#         if not self.is_started:
#             print("Engine not started.")
#             self.is_started = False
#         else:
#             print("Engine is not running.")

#     def stop_engine(self):
#         if self.is_started:
#             print("Engine not stopped.")
#             self.is_started = True
#         else:
#             print("Engine is not stopped.")

#     def get_car_details(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")
#         print(f"Engine status: {'Running' if self.is_started else 'Stopped'}")


# # Create an instance of the Car class
# my_car = Car("Toyota", "Camry", 2022)

# # Access class members and call methods
# my_car.start_engine()
# my_car.get_car_details()

# my_car.stop_engine()
# my_car.get_car_details()
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)

# # Create an object of the Rectangle class
# rect = Rectangle(5, 3)

# # Access and print the attributes of the object
# print("Length:", rect.length)
# print("Width:", rect.width)

# # Call the methods of the object
# area = rect.calculate_area()
# perimeter = rect.calculate_perimeter()

# print("Area:", area)
# print("Perimeter:", perimeter)


# # 2 Write a program to implement default constructor, parameterized constructor, 
# # and destructor. 
# class MyClass:
#     def __init__(self):
#         print("Default constructor called.")

#     def __init__(self, parameter):
#         self.parameter = parameter
#         print("Parameterized constructor called.")

#     def __del__(self):
#         print("Destructor called.")

# # Creating objects using different constructors
# obj1 = MyClass()  # Default constructor called

# obj2 = MyClass("Hello")  # Parameterized constructor called

# del obj1  # Destructor called
# del obj2  # Destructor called

# # 3. Create a Python class named Rectangle constructed by a length and width.

# class Rectangle:
#     def __init__(self,l,w):
#         self.length=l
#         self.width=w
# def area(self):
#     return self.length*self.width
# l = int(input('Enter length '))
# w = int(input('Enter width '))
# rect = Rectangle(l,w)
# print('Area = ',rect.area())

# # 4. MULTIPLIER, and a constructor which takes the parameters x and y (these 
# # should all be numbers). 
# # a. Write an instance method called add which returns the sum of the 
# # attributes x and y. 
# # b. Write a class method called multiply, which takes a single number 
# # parameter a and returns the product of a and MULTIPLIER. 
# # c. Write a static method called subtract, which takes two number objects, b 
# # and c, and returns b - c. 
# # d. Write a method called value which returns a tuple containing the values of x 
# # and y

# class Number:
#     MULTIPLIER = 10

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def add(self):
#         return self.x + self.y

#     @classmethod
#     def multiply(cls, a):
#         return a * cls.MULTIPLIER

#     @staticmethod
#     def subtract(b, c):
#         return b - c

#     def value(self):
#         return (self.x, self.y)
    
# #5.Create a class named as Student to store the name and marks in three 
# # subjects. Use List to store the marks. 
# # a. Write an instance method called compute to compute total marks and 
# # average marks of a student. 
# # b. Write a method called display to display student information.
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.marks = []
#     def setmarks(self):
#         m=input("enter marks of 3 subjects").split()
#         marks=[int(i)for i in m]
#         self.marks=marks
#     def compute(self):
#         totalmarks=0
#         for m1 in self.marks:
#             totalmarks = m1+totalmarks
#         average_marks = totalmarks / len(self.marks)
#         print(totalmarks) 
#         print(average_marks)

#     def display(self):
#         print("Student Name:", self.name)
#         print("Marks:", self.marks)
# p=input("name: ")
# st=Student(p)
# st.setmarks()
# st.compute()
# st.display()
# # Create a class Employee that keeps a track of the number of employees in an 
# # organization and also stores their name, designation and salary details. 
# # a. Write a method called getdata to take input (name, designation, salary) 
# # from user. 
# # b. Write a method called average to find average salary of all the employees 
# # in the organization. 
# # c. Write a method called display to print all the information of an employee. 

# class Employee:
#     count = 0

#     def __init__(self, name, designation, salary):
#         self.name = name
#         self.designation = designation
#         self.salary = salary
#         Employee.count += 1

#     @classmethod
#     def getdata(cls):
#         name = input("Enter employee name: ")
#         designation = input("Enter employee designation: ")
#         salary = float(input("Enter employee salary: "))
#         return cls(name, designation, salary)

#     @staticmethod
#     def average(employees):
#         total_salary = sum(emp.salary for emp in employees)
#         avg_salary = total_salary / len(employees)
#         return avg_salary

#     def display(self):
#         print("Employee Information:")
#         print("Name:", self.name)
#         print("Designation:", self.designation)
#         print("Salary:", self.salary)

# employees=[]
# count=int(input('no. of employess: '))
# for i in range(count):
#     employee=Employee.getdata()
#     employees.append(employee)
# for employee in employees:
#     employee.display()
# avg_salary=Employee.average(employees)
# print('average salary is:',avg_salary)


# # 7.Create a Python class named Circle constructed by a radius. Use a class 
# # variable to define the value of constant PI. 
# # a. Write two methods to be named as area and circum to compute the area 
# # and the perimeter of a circle respectively by using class variable PI. 
# # b. Write a method called display to print area and perimeter. 
# class Circle:
#     PI = 3.14159

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return Circle.PI * (self.radius ** 2)

#     def circum(self):
#         return 2 * Circle.PI * self.radius

#     def display(self):
#         print("Circle Information:")
#         print("Radius:", self.radius)
#         print("Area:", self.area())
#         print("Perimeter:", self.circum())

# # 8.Create a class called String that stores a string and all its status details such as 
# # number of uppercase letters, lowercase letters, vowels ,consonants and space 
# # in instance variables. 
# # a. Write methods named as count_uppercase, count_lowercase, 
# # count_vowels, count_consonants and count_space to count corresponding 
# # values. 
# # b. Write a method called display to print string along with all the values 
# # computed by methods in (a).

# class String:
#     def __init__(self, string):
#         self.string = string
#         self.uppercase_count = 0
#         self.lowercase_count = 0
#         self.vowel_count = 0
#         self.consonant_count = 0
#         self.space_count = 0

#     def count_uppercase(self):
#         for char in self.string:
#             if char.isupper():
#                 self.uppercase_count += 1

#     def count_lowercase(self):
#         for char in self.string:
#             if char.islower():
#                 self.lowercase_count += 1

#     def count_vowels(self):
#         vowels = ['a', 'e', 'i', 'o', 'u']
#         for char in self.string.lower():
#             if char in vowels:
#                 self.vowel_count += 1

#     def count_consonants(self):
#         consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
#         for char in self.string.lower():
#             if char in consonants:
#                 self.consonant_count += 1

#     def count_space(self):
#         for char in self.string:
#             if char.isspace():
#                 self.space_count += 1

#     def display(self):
#         print("String:", self.string)
#         print("Uppercase Letters:", self.uppercase_count)
#         print("Lowercase Letters:", self.lowercase_count)
#         print("Vowels:", self.vowel_count)
#         print("Consonants:", self.consonant_count)
#         print("Spaces:", self.space_count)
# S=String('PAlak')
# S.count_uppercase()
# S.count_lowercase()
# S.count_vowels()
# S.count_consonants()
# S.count_space()
# S.display()
# # 9.Write a program that has a class called Fraction with attributes numerator and 
# # denominator. 
# # a. Write a method called getdata to enter the values of the attributes. 
# # b. Write a method show to print the fraction in simplified form

# class Fraction:
#     def __init__(self):
#         self.numerator = 0
#         self.denominator = 0

#     def getdata(self):
#         self.numerator = int(input("Enter the numerator: "))
#         self.denominator = int(input("Enter the denominator: "))

#     def show(self):
#         gcd = self.calculate_gcd(self.numerator, self.denominator)
#         simplified_numerator = self.numerator // gcd
#         simplified_denominator = self.denominator // gcd
#         print("Fraction: {}/{}".format(simplified_numerator, simplified_denominator))

#     @staticmethod
#     def calculate_gcd(a, b):
#         while b != 0:
#             a, b = b, a % b
#         return a
# # 10.Write a program that has a class Numbers with a list as an instance variable. 
# # a. Write a method called insert_element that takes values from user. 
# # b. Write a class method called find_max to find and print largest value in the 
# # list

# class Numbers:
#     def __init__(self):
#         self.list1 = []
#     def insert_element(self):
#         val = int(input('Enter value '))
#         self.list1.append(val)
#     def find_max(self):
#         if len(self.list1)>0:
#             max1 = self.list1[0]
#             for i in range(1,len(self.list1)):
#                 if max1<self.list1[i]:
#                     max1 = self.list1[i]
#             return max1
#         else:
#             return 'Empty List!'
# num = Numbers()
# num.insert_element()
# num.insert_element()
# num.insert_element()
# num.insert_element()
# print(num.list1)
# print('Maximum Value =',num.find_max())

# # 11.Write a program that has a class Point with attributes x and y
# # Write a method called midpoint that returns a midpoint of a line joining two points. b) Write a method called length that returns the length of
# # a line joining two points.

# class point:
#     def midpoint(self, point1, point2):
#         x1, y1 = point1
#         x2, y2 = point2
#         midpoint_x = (x1 + x2) / 2
#         midpoint_y = (y1 + y2) / 2
#         return midpoint_x, midpoint_y

#     def length(self, point1, point2):
#         x1, y1 = point1
#         x2, y2 = point2
#         dx = x2 - x1
#         dy = y2 - y1
#         distance = (dx ** 2 + dy ** 2) ** 0.5
#         return distance

# line = point()
# point1 = (2, 3)
# point2 = (6, 8)
# midpoint = line.midpoint(point1, point2)
# length = line.length(point1, point2)

# print("Midpoint:", midpoint)
# print("Length:", length)

# # 12.Create a class called Complex. Write a menu driven program to read,display, add and subtract two complex numbers by
# # creating corresponding instance methods
# class Complex:
#     def __init__(self, real=0, imaginary=0):
#         self.real = real
#         self.imaginary = imaginary

#     def read_complex(self):
#         self.real = float(input("Enter the real part: "))
#         self.imaginary = float(input("Enter the imaginary part: "))

#     def display_complex(self):
#         print("Complex number:", self.real, "+", self.imaginary, "i")

#     def add_complex(self, num1, num2):
#         real_sum = num1.real + num2.real
#         imaginary_sum = num1.imaginary + num2.imaginary
#         result = Complex(real_sum, imaginary_sum)
#         return result

#     def subtract_complex(self, num1, num2):
#         real_diff = num1.real - num2.real
#         imaginary_diff = num1.imaginary - num2.imaginary
#         result = Complex(real_diff, imaginary_diff)
#         return result


# # Example usage:
# complex1 = Complex()
# complex1.read_complex()
# complex1.display_complex()

# complex2 = Complex()
# complex2.read_complex()
# complex2.display_complex()

# choice = input("Enter 1 to add, 2 to subtract: ")

# if choice == '1':
#     sum_result = complex1.add_complex(complex1, complex2)
#     print("Sum:")
#     sum_result.display_complex()
# elif choice == '2':
#     diff_result = complex1.subtract_complex(complex1, complex2)
#     print("Difference:")
#     diff_result.display_complex()
# else:
#     print("Invalid choice.")

# #13. Write a Program to illustrate the use of str,repr and new
# class Myclass:
#     def __new__(cls):
#         print ("__new__ magic method is called")
#         inst = object.__new__(cls)
#         return inst
#     def __init__(self):
#         print ("__init__ magic method is called")
#         self.name='Python'
# myobj = Myclass()
# print(myobj.name)
# # __new__ magic method is called
# # __init__ magic method is called
# # Destructing object.
# # Python
# class Employee:
#     def __init__(self):
#         self.name='Anu'
#         self.salary=60000
#     def __str__(self):
#         return 'Name = ' + self.name + ', Salary=₹'+str(self.salary)
#     def __repr__(self):
#         return 'Hello = ' + self.name
# emp = Employee()
# print(emp)
# print(repr(emp))

# #14.Create a BankAccount class. Your class should support the following 
# #  a)__init__(self, account_no) b) deposit (self, amount) c) withdraw (self, amount) d) get_balance (self)

# class BankAccount:
#     def __init__(self,account_no):
#         self.account_no = account_no
#         self.balance = 0
#     def deposit(self,amount):
#         self.balance = self.balance + amount
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Alert! Insuffcient balance")
#         else:
#             self.balance = self.balance - amount
#     def get_balance(self):
#         print("Account Number :",self.account_no)
#         print("Balance Amount :",self.balance)
# a = int(input('Enter Account Number '))
# c1 = BankAccount(a)
# c1.get_balance()
# amount = int(input('Enter amount to be deposited '))
# c1.deposit(amount)
# c1.get_balance()
# amount = int(input('Enter amount to be withrawn '))
# c1.withdraw(amount)
# c1.get_balance()

# #15 Write a program to illustrate the use of following built-in methods:
# #  hasattr(obj,attr) b) getattr(object, attribute_name [, default]) c) setattr(object, name, value) d) delattr(class_name, name)
# class MyClass:
#     def __init__(self):
#         self.name = "John"
#         self.age = 25

# # Creating an object of MyClass
# obj = MyClass()

# # Using hasattr to check if an attribute exists
# print(hasattr(obj, 'name'))  # Output: True
# print(hasattr(obj, 'address'))  # Output: False

# # Using getattr to get the value of an attribute
# print(getattr(obj, 'name'))  # Output: John
# print(getattr(obj, 'address', 'Not Found'))  # Output: Not Found (default value)

# # Using setattr to set the value of an attribute
# setattr(obj, 'age', 30)
# print(getattr(obj, 'age'))  # Output: 30

# # Using delattr to delete an attribute
# delattr(obj, 'name')
# print(hasattr(obj, 'name'))  # Output: False

# #16 Write a program to create class Employee. Display the personal information and salary details of 5 employees using single
# # inheritance

# class Employee:
#     def __init__(self, name, age, address, salary):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.salary = salary

#     def display_personal_info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Address:", self.address)

#     def display_salary_details(self):
#         print("Salary:", self.salary)


# # Creating a derived class called Manager
# class Manager(Employee):
#     def __init__(self, name, age, address, salary, department):
#         super().__init__(name, age, address, salary)
#         self.department = department

#     def display_department(self):
#         print("Department:", self.department)


# # Creating instances of the Manager class
# manager1 = Manager("John Doe", 35, "123 Main St", 5000, "Finance")
# manager2 = Manager("Jane Smith", 40, "456 Elm St", 6000, "Marketing")
# manager3 = Manager("David Johnson", 45, "789 Oak St", 5500, "HR")
# manager4 = Manager("Sarah Williams", 38, "987 Pine St", 5200, "Operations")
# manager5 = Manager("Michael Brown", 42, "654 Maple St", 5800, "Sales")

# # Displaying personal information and salary details of 5 employees
# manager1.display_personal_info()
# manager1.display_salary_details()
# manager1.display_department()
# print()

# manager2.display_personal_info()
# manager2.display_salary_details()
# manager2.display_department()
# print()

# manager3.display_personal_info()
# manager3.display_salary_details()
# manager3.display_department()
# print()

# manager4.display_personal_info()
# manager4.display_salary_details()
# manager4.display_department()
# print()

# manager5.display_personal_info()
# manager5.display_salary_details()
# manager5.display_department()

# #17.WAP that extends the class Employee. Derive two classes Manager and Team Leader from Employee class. Display all the
# # details of the employee working under a particular Manager and Team Leader.
# class Employee:
#     def __init__(self, name, employee_id):
#         self.name = name
#         self.employee_id = employee_id

#     def display_details(self):
#         print("Employee Name:", self.name)
#         print("Employee ID:", self.employee_id)


# class Manager(Employee):
#     def __init__(self, name, employee_id, department):
#         super().__init__(name, employee_id)
#         self.department = department
#         self.employees = []

#     def add_employee(self, employee):
#         self.employees.append(employee)

#     def display_details(self):
#         super().display_details()
#         print("Department:", self.department)
#         print("Employees under this Manager:")
#         for employee in self.employees:
#             employee.display_details()
#         print()


# class TeamLeader(Employee):
#     def __init__(self, name, employee_id, team):
#         super().__init__(name, employee_id)
#         self.team = team
#         self.employees = []

#     def add_employee(self, employee):
#         self.employees.append(employee)

#     def display_details(self):
#         super().display_details()
#         print("Team:", self.team)
#         print("Employees under this Team Leader:")
#         for employee in self.employees:
#             employee.display_details()
#         print()


# # Create Employees
# employee1 = Employee("John Doe", 1001)
# employee2 = Employee("Jane Smith", 1002)
# employee3 = Employee("David Johnson", 1003)
# employee4 = Employee("Sarah Williams", 1004)

# # Create Manager
# manager = Manager("Michael Brown", 2001, "Finance")
# manager.add_employee(employee1)
# manager.add_employee(employee2)

# # Create Team Leader
# team_leader = TeamLeader("Jessica Davis", 3001, "Development")
# team_leader.add_employee(employee3)
# team_leader.add_employee(employee4)

# # Display details
# manager.display_details()
# team_leader.display_details()

# # 18 Write a program that has a class Point. Define another class Location which has two objects (origin and destination) of
# # class Point. Also, define a function in Location that prints the reflection on the y-axis
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def display(self):
#         print("Point: ({}, {})".format(self.x, self.y))


# class Location:
#     def __init__(self, origin, destination):
#         self.origin = origin
#         self.destination = destination

#     def print_reflection(self):
#         reflected_x = -self.destination.x
#         reflected_y = self.destination.y
#         reflected_point = Point(reflected_x, reflected_y)
#         print("Reflection on the y-axis:")
#         reflected_point.display()


# # Create the Point objects
# origin = Point(0, 0)
# destination = Point(3, 4)

# # Create the Location object
# location = Location(origin, destination)

# # Print the reflection
# location.print_reflection()

# #19. WAP that create a class Student having attribute as name and age and Marks class inheriting Students class with its own attributes marks1, marks2 and marks3 as marks in 3 subjects. Also, define the class Result that inherits the 
# # Marks class with its own attribute total. Every class has its own display() 
# # method to display the corresponding details. Use __init__() and super() to 
# # implement the above classes

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# class Marks(Student):
#     def __init__(self, name, age, marks1, marks2, marks3):
#         super().__init__(name, age)
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3

#     def display(self):
#         super().display()
#         print("Marks 1:", self.marks1)
#         print("Marks 2:", self.marks2)
#         print("Marks 3:", self.marks3)


# class Result(Marks):
#     def __init__(self, name, age, marks1, marks2, marks3):
#         super().__init__(name, age, marks1, marks2, marks3)
#         self.total = marks1 + marks2 + marks3

#     def display(self):
#         super().display()
#         print("Total:", self.total)


# # Create a Student object
# student = Student("John Doe", 20)
# student.display()
# print()

# # Create a Marks object
# marks = Marks("Jane Smith", 22, 90, 85, 95)
# marks.display()
# print()

# # Create a Result object
# result = Result("David Johnson", 21, 80, 75, 85)
# result.display()

# #20 Write a program that create a class Distance with members km and metres.Derive classes School and office which store the distance from your house to school and office along with other details. 

# class Distance:
#     def __init__(self, km, metres):
#         self.km = km
#         self.metres = metres


# class School(Distance):
#     def __init__(self, km, metres, name):
#         super().__init__(km, metres)
#         self.name = name

#     def display_details(self):
#         print("School Name:", self.name)
#         print("Distance from House to School:", self.km, "km", self.metres, "metres")


# class Office(Distance):
#     def __init__(self, km, metres, address):
#         super().__init__(km, metres)
#         self.address = address

#     def display_details(self):
#         print("Office Address:", self.address)
#         print("Distance from House to Office:", self.km, "km", self.metres, "metres")


# # Create an instance of School class
# school = School(5, 500, "ABC School")
# school.display_details()
# print()

# # Create an instance of Office class
# office = Office(10, 200, "XYZ Office")
# office.display_details()


# Decorator function to add a 'greet' method to the class


# def add_greet_method(cls):
#     def greet(self):
#         return f"Hello, I am a {self.name} instance!"
#     cls.greet = greet
#     return cls

# # Applying the decorator to a class
# @add_greet_method
# class MyClass:
#     def __init__(self, name):
#         self.name = name

# # Creating an instance of the decorated class
# obj = MyClass("John")
# print(obj.greet())  # Output: Hello, I am a MyClass instance!


def reverse_string(string):
    length = len(string)
    for i in range(length - 1, -1, -1):
        yield string[i]

# Using the reverse_string generator to reverse a string
my_string = "Hello, World!"
reversed_str = ''.join(reverse_string(my_string))

print(reversed_str)  # Output: "!dlroW ,olleH"
