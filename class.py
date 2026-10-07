# 1
class StudentProfile:
    def __init__(self, name, age, grade, auid):
        self.name = name
        self.age = age
        self.grade = grade
        self.auid = auid

    def __str__(self):
        return f"Ism: {self.name}, Yoshi: {self.age}, Bosqich: {self.grade}, AUID: {self.auid}"


name = "O'tkirbek"
age = "18"
grade = "2"
AUID = "ABT25CCS001"

student = StudentProfile(name, age, grade, AUID)
print(student)

# 2
class Teacher:
    def __init__(self, name, subject, experience, salary):
        self.name = name
        self.subject = subject
        self.experience = experience
        self.salary = salary

    def __str__(self):
        return f"O'qituvchi: {self.name}, Fan: {self.subject}, Tajriba: {self.experience}, Maosh: {self.salary}"


name = "Gulap"
subject = "Data Structure"
experience = "2 year"
salary = "100$"

teach = Teacher(name, subject, experience, salary)
print(teach)


# 3
class Car:
    def __init__(self, model, year, color, price):
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.model} {self.year} {self.color}  {self.price}"


model = "Mers"
year = "2022"
color = "Black"
price = "20000$"

car = Car(model, year, color, price)
print(car)


# 4
class Phone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB)  {self.price}$"


brand = "Apple"
model = "iPhone 15"
storage = "256"
price = "159"

ph = Phone(brand, model, storage, price)
print(ph)


# 5
class Book:
    def __init__(self, title, author, year, ):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' {self.author} {self.year}"


title = "Python Basics"
author = "John Doe"
year = "2024"

b = Book(title, author, year,)
print(b)


# 6
class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Egasi: {self.owner}, Hisob: {self.account_number}, Balans: {self.balance}"


owner = "Ali"
account_number = "8600 1234 5678 9012"
balance = "50000$"

acc = BankAccount(owner, account_number, balance)
print(acc)


# 7
class Pizza:
    def __init__(self, name, size, price, ingredients):
        self.name = name
        self.size = size
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.size} {self.name} pizza  {self.price}$  Tarkibi: {', '.join(self.ingredients)}"


name = "Pepperoni"
size = "Large"
price = "12"
ingredients = ["pishloq", "pomidor"]

pz = Pizza(name, size, price, ingredients)
print(pz)


# 8
class Animal:
    def __init__(self, name, age,):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}  {self.age} yosh"

name = "Rex"
age = "3"

a = Animal(name,  age, )
print(a)


# 9
class Film :
    def __init__(self, title,  year,):
        self.title = title
        self.year = year
    def __str__(self):
        return f"'{self.title}' {self.year}"


title = "Inception"
year = '2010'

m = Film(title, year,)
print(m)


# 10
class Football:
    def __init__(self, club, year):
        self.club = club
        self.year = year

    def __str__(self):
        return f"{self.club} {self.year} yil"


club = "REAL MADRID"
year = "10"

f = Football(club, year)
print(f)
# 11
class House:
    def __init__(self, address, rooms,):
        self.address = address
        self.rooms = rooms

    def __str__(self):
        return f"{self.address} {self.rooms} xona,"


address = "Tashkent, Chilonzor"
rooms = "6"

h = House(address, rooms,)
print(h)


# 12
class Coffee:
    def __init__(self, type_, price):
        self.type = type_
        self.price = price

    def __str__(self):
        return f"{self.type}  {self.price}$"


type_ = "Capucino"
price = "2"

cof = Coffee(type_, price)
print(cof)


# 13
class Taxi:
    def __init__(self, driver, car,):
        self.driver = driver
        self.car = car


    def __str__(self):
        return f"Haydovchi: {self.driver} Mashina: {self.car} "

driver = "Sardor"
car = "Cobalt"


tax = Taxi(driver, car,)
print(tax)


# 14
class Game:
    def __init__(self, name, genre,):
        self.name = name
        self.genre = genre
    def __str__(self):
        return f"{self.name} {self.genre}"


name = "Minecraft"
genre = "Sandbox"

g = Game(name, genre,)
print(g)


# 15
class Weather:
    def __init__(self, city, temperature, ):
        self.city = city
        self.temperature = temperature

    def __str__(self):
        return f"{self.city} {self.temperature}°C"


city = "Toshkent"
temperature = "32"


w = Weather(city, temperature,)
print(w)


# 16
class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.name} {self.location}"


name = "Milliy Taomlar"
location = "Buxoro"


r = Restaurant(name,location)
print(r)


# 17
class TV:
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price

    def __str__(self):
        return f"{self.brand} TV  O'lcham:{self.size} {self.price}$"


brand = "Samsung"
size = "55"
price = "300"

tv = TV(brand, size, price)
print(tv)


# 18
class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def __str__(self):
        return f"{self.brand}  {self.ram}GB RAM, {self.storage}GB, {self.price}$"


brand = "HP Victus"
ram = "8"
storage = "512"
price = "900"

lap = Laptop(brand, ram, storage, price)
print(lap)


# 19
class Shoes:
    def __init__(self, brand, size,):
        self.brand = brand
        self.size = size

    def __str__(self):
        return f"{self.brand} size {self.size}"


brand = "Nike"
size = "39"

sh = Shoes(brand, size,)
print(sh)


# 20
class Country:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"{self.name} maydoni: {self.area} km²"

name = "O'zbekiston"
area = "448978"

cnt = Country(name, area)
print(cnt)

