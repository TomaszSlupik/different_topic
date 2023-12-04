# ćw 1 sortowanie po wieku 
class Person:
    def __init__(self, firstName, age):
        self.firstName = firstName
        self.age = age

people = [
    Person("Tom", 25),
    Person("John", 29),
    Person("Mike", 27),
    Person("Alice", 19)
]

sortedForAge = sorted(people, key=lambda x: x.age)

for sortPeople in sortedForAge:
    print (f"{sortPeople.firstName} -> {sortPeople.age}")
print('---')

# ćw 2 resetowanie x, y i przypisanie wartości x = 0 i y = 0
class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    def reset(self):
        self.x = 0
        self.y = 0


    
point = Point(4, 2)
print(point)
point.reset()
print(point)
print('---')

# ćw3 Odległość dwóch punktów od siebie
import math
class Distance():
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def calc_distance(self, other):
        return math.sqrt (
            (self.first - other.first) ** 2 + (self.second - other.second) ** 2
        )


distanceOne = Distance(0, 3)
distanceTwo = Distance(4, 0)
print(distanceOne.calc_distance(distanceTwo))
print('---')

# ćw 4 - Notatki + data utworzenia notatek
import datetime 

class Note ():
    def __init__(self, note):
        self.note = note
        self.creation_time = datetime.datetime.now()

    def content(self):
        return f"{self.note}"

    def getcreation_time (self):
        return self.creation_time.strftime('%m-%d-%Y %H:%M:%S')
    
note1 = Note('My first note.')
note2 = Note('My second note.')

print(note1.content())
print(note2.content())
print ("Data utworzenia notatek:", note1.getcreation_time())
print('---')

# ćw 5 Sprawdzenie słowa 'Python' - wielkość liter ma znaczenie
class Checkword ():
    def __init__(self, word):
        self.word = word

    def find(self, findWord):
        return findWord in self.word
    
checkOne = Checkword('Object Oriented Programming in Python.')

print(checkOne.find('python'))
print(checkOne.find('Python'))
print('---')

# ćw 6 wielkość liter nie ma znaczenie
class CheckLower ():
    def __init__(self, word):
        self.word = word

    def find(self, find):
        return find.lower() in self.word.lower()
    
checkTwo = CheckLower('Object Oriented Programming in Python.')
print (checkTwo.find('python'))
print (checkTwo.find('Python'))
print('---')

# ćw 7 Notebook - dodanie do listy notatek
class Notebook ():
    def __init__(self):
        self.notes = []

    def new_note(self, myNote):
        self.notes.append(myNote)
    
    def __repr__(self):
        return f"Note(content={self.notes})"
    
notebook =  Notebook()  


notebook.new_note('My first note.')
notebook.new_note('My second note.')

print (notebook.notes)
print('---')

# ćw 8 Wiele argumentów *args
class Date ():
    def __init__(self, *specialize):
        self.specialize = specialize
    
    def search(self):
        return f"{self.specialize}"
    
date = Date('Big Data', 'Data Science', 'Machine Learning')

print(date.search())
print('---')


# ćw 9 Unpacking - rozpakowywanie 
number = (45, 23, 14)
a, b, c = number

x = number[0]
print (f"Szybszy sposób: {a}, lub tradycyjny sposób: {x}")
print('---')

# ćw 10 Dodanie klientów do jednej tablicy 
class Client():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def all_clients (self):
        return [self.name, self.email]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}',email: '{self.email}')"
    
client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@yahoo.com')
client3 = Client('Mike', 'sales-contact@yahoo.com') 

allClient = [client1, client2, client3]
clients= []

for client in allClient:
    clients.append(client)

print(clients)
print('---')

# ćw 11
# **kwars dowolna liczba elementów i wyświetlenie values
# Również można wyświetlić keys 
class Person():
    def concatenate_strings (self, **kwargs):
        concatenated = ",".join(str(value) for value in kwargs.values())
        return concatenated
        
person = Person()

firstPerson_result = person.concatenate_strings(first_name='John', last_name='Doe', age=30)
secondPerson_result = person.concatenate_strings()
thirdPerson_result = person.concatenate_strings(first_name='Mary', gender='Female')
fourthPerson_result = person.concatenate_strings(first_name='Mary', gender='Female', age=5)

print(firstPerson_result)
print(secondPerson_result)
print(thirdPerson_result)
print (fourthPerson_result)
print('---')

# ćw 12 LEGB: możliwość posiadania wielu zmiennych o tej samej nazwie w różnych zakresach.
# Wynik będzie 10
x = 10
def func1():
    y = 5
    return y

def func2():
    y = 2
    return func1() * y

print(func2())
print('---')

# ćw 13 LEGB - wynik 50 => wywołanie globals tj. 5 * 10
a = 10
def func1():
    a = 5
    return a

def func2():
    a = 2
    return func1() * globals()['a']

print(func2())
print('---')

# ćw 14 LEGB => global zamian na 5
y = 10

def func1():
    global y 
    y = 5

def func2():
    print (y) 


func1()
func2()
print('---')

# ćw 15 Nonlocal - i zmiana wartości na 7, a Global => wartość 10
x = 10
def func1():
    x = 5

    def inner_func():
        nonlocal x
        x = 7
        
    inner_func()

    print(x)

def func2():
    global x 
    print(x)

func1()
func2()
print('---')

# ćw 16 - ten przykład: wyniki 20 i 20, bo jest wewenątrz inner_function 
# i daliśmy nonlocal 
def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x = 20
        print("Inner function:", x)

    inner_function()
    print("Outer function:", x)

outer_function()
print('---')

# ćw 17 _ do odczytu i modyfikacji, dekorator - @property - do oczytu
# Obliczenie pola prostokątu
class Rectangle():
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area (self):
        return self._width * self._height        
    
rectangle = Rectangle(3, 4)

print (f"width: {rectangle._width}, height: {rectangle._height} -> area: {rectangle.area}")
print('---')

# ćw 18
# Obliczenie obwodu prostokąta 

class Oblong ():
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
    
    def perimeter(self):
        return 2 * (self.heigth + self.width)

    def __repr__(self):
        return f"width: {self.width}, height: {self.heigth} -> perimeter: {self.perimeter()}"
    

oblong = Oblong(3, 4)

print(oblong)
print('---')

# ćw 19 - gettery czyli odczyt prywatnej wartości atrybutu
# oznaczony dekoratorem @property
# look jest geterem i pozwala odczytać wartość prywatną atrybutu

class MyClass():
    def __init__(self, length):
        self._length = length

    @property
    def look(self):
        return self._length
    
obj = MyClass(10)

print(obj.look)
print('---')

# ćw 20 - settery czyli możliwość zmiany wartości prywatnej 

class Timer ():
    def __init__(self, time):
        self._time = time

    @property
    def myTime(self):
        return self._time
    
    @myTime.setter
    def myTime(self, value):
        if isinstance(value, int):
            self._time = value
            print(f"Wpisałeś poprawnie, twój czas to: {self._time} min")
        else:
            print("Wpisz liczbę jako int")

myobj = Timer(90)

myobj.myTime = 100
print('---')

# ćw 21
# gettery i settery 

class Circle ():
    def __ini__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value

    def perimeter (self):
        return f"Obwód koła wynosi: {2 * 3.14 * self._radius}"

circle = Circle()
circle.radius = 3

print(circle.perimeter())
print('---')

# Dodawanie samych stringów do listy
class StringListOnly (): 
    def __init__(self, thisName):
        self.thisName = thisName
        self.listStr = []

    def appendToList(self):
        if isinstance(self.thisName, str):
            self.listStr.append(self.thisName)
        else:
            raise TypeError ('Only objects of type str can be added to the list.')


firstString = StringListOnly('Data')
firstString.appendToList()

secondString = StringListOnly('Science')
secondString.appendToList()

thirdString = StringListOnly('Machine Learning')
thirdString.appendToList()

print(f"{firstString.listStr}, {secondString.listStr}, {thirdString.listStr}")
print("---")

# Produkty z pustą tablicą

class Product():
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

class Warehouse(Product):
    def __init__(self):
        self.products  = []


warehouse = Warehouse()
print(warehouse.products)
print("---")

# dodawanie produktów, gdy są duplikaty pomijamy 
class ParamiterProduct ():
    def __init__(self, nameProduct, priceProduct):
        self.nameProduct = nameProduct
        self.priceProduct = priceProduct

class Addproduct(ParamiterProduct):
    def __init__(self):
        self.check_product = []

    def add_product_to_list(self, products):
        for check in self.check_product:
            if check.nameProduct == products.nameProduct and check.priceProduct == products.priceProduct:
                print("Produkt istnieje")
                return
        self.check_product.append(products)

all_product = Addproduct()

firstProduct = ParamiterProduct('Laptop', 3900.0)
secondProduct = ParamiterProduct('Mobile Phone', 1990.0)
thirdProduct = ParamiterProduct('Mobile Phone', 1990.0)

all_product.add_product_to_list(firstProduct)
all_product.add_product_to_list(secondProduct)
all_product.add_product_to_list(thirdProduct)

print("Lista produktów które zostały dodane:")
for item in all_product.check_product:
    print(f"{item.nameProduct} z ceną {item.priceProduct}")

print("---")

# Dodawanie i usuwanie produktów z koszyka:
class ProductSettings ():
    def __init__(self, nameProduct, priceProduct):
        self.nameProduct = nameProduct
        self.priceProduct = priceProduct

    def __repr__(self) -> str:
        return f"{self.nameProduct} => {self.priceProduct}"

class ProductLogic():
    
    def __init__(self):
        self.productList = []

    def addProduct (self, nameProduct, priceProduct):
        product = ProductSettings(nameProduct, priceProduct)
        self.productList.append(product)

    def removeProduct (self, nameProduct):
        self.productList = [product for product in self.productList if product.nameProduct != nameProduct]

    def __repr__(self) -> str:
        return f"Lista produktów {self.productList}"


productLogic = ProductLogic()
productLogic.addProduct('Laptop', 3900.0)
productLogic.addProduct('Smartphone', 1200.0)
productLogic.addProduct('Iphone 14 PRO', 5000.0)

productLogic.removeProduct('Smartphone')

print (productLogic)

print("---")

# Nieformalna reprezentacja obiektu __str__
class Training ():
    def __init__(self, kind, time):
        self.kind = kind
        self.time = time

    def __str__(self) -> str:
        return f"{self.__class__.__name__} => {self.kind}, czas trwania: {self.time} min"
    

myTraining = Training('Pływanie', 70)

print(myTraining)
print("---")

# sortowanie produktów 
class Phone ():
    def __init__(self, phone, price):
        self.phone = phone
        self.price = price

class PhoneList ():
    def __init__(self):
        self.listPhone = []

    def appendPhone(self, apendPhone):
        product = [apendPhone.phone, apendPhone.price]
        self.listPhone.append(product)
    
    def sortPhone(self, ascending=True):
        self.listPhone.sort(key=lambda x: x[1], reverse=not ascending)

    def __str__(self) -> str:
        return f"Lista telefonów: {self.listPhone}"


phoneList = PhoneList()

phoneFirst = Phone('Iphone', 13)
phoneSecond = Phone('Iphone', 14)
phoneThird = Phone('Iphone', 12)

phoneList.appendPhone(phoneFirst)
phoneList.appendPhone(phoneSecond)
phoneList.appendPhone(phoneThird)

phoneList.sortPhone(ascending=True)
print(phoneList)
print("---")

# wyszukiwarka - 1 przykład
class Competition():
    def __init__(self, nameCompetition):
        self.nameCompetition = nameCompetition

class AllCompetitions():
    def __init__(self):
        self.ListCompetition = []

    def append(self, name):
        self.ListCompetition.append(name.nameCompetition)

    def search(self, world):
        for name in self.ListCompetition:
            if world in name:
                print ({name})
    
    def __str__(self) -> str:
        return f"{self.ListCompetition}"

allCompetitions = AllCompetitions()

firstCompetition = Competition('Bieganie')
secondCompetition = Competition('Rower')
thirdCompetiton = Competition('Pływanie')
fourthCompetiton = Competition('Siłownia')

myList = [firstCompetition, secondCompetition, thirdCompetiton, fourthCompetiton]

for name in myList:
    allCompetitions.append(name)

print(allCompetitions)

print ('---')

print ('Wyszukiwarka:')
# szukamy w słowach danych liter
allCompetitions.search('Pł')

# wyszukiwarka - 2 przykład
class ClientList (list):
    def search_email(self, value):
        match_client = [client for client in self if value in client.email]
        return match_client


class Client:
    all_clients = ClientList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    def __repr__(self) -> str:
        return f"Client(name='{self.name}', email='{self.email}')"
    
client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@gmail.com')
client3 = Client('Mike', 'sales@yahoo.com')
client4 = Client('Lisa', 'info@gmail.com')

print(Client.all_clients)
# Wyświetlenie tylko e-mail ze słowem sales 
print(Client.all_clients.search_email('sales'))
print("---")

# Wyszukanie jeden pod drugim Nazwy + email
emailWithGmail = Client.all_clients.search_email('gmail')

for gmail in emailWithGmail:
    print(gmail)
print("---")

# Wyszukanie samych klientów posiadających w nazwie adresu mailowego słówko 'sales'
onlySales = Client.all_clients.search_email('sales')
clientsWithSales = []

for sales in onlySales:
    clientsWithSales.append(sales.name)
print(clientsWithSales)
print("---")


# Sprawdzenie czy są to Stringi, w przeciwnym wypadku False 
class CustomDict ():
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    def is_any_str_value(self):
        return any(isinstance(value, str) for value in self.kwargs.values())

cd = CustomDict(python='mid')
cdTwo = CustomDict(price=119.99)
print(cd.is_any_str_value())
print(cdTwo.is_any_str_value())
print("---")

# Dodawanie tylko Stringów
class StringCheck():
    def __init__(self, nameString):
        self.nameString = nameString
    def __str__(self) -> str:
        return f"{self.nameString}"

class StringListOnly ():
    def __init__(self):
        self.onlyString = []

    def append(self, value):
        if isinstance(value, str):
            self.onlyString.append(value)
        else:
            raise TypeError ("Only objects of type str can be added to the list.")

    def display(self):
        for item in self.onlyString:
            print (item)

stringListOnly = StringListOnly()

firstCheck = 'Data'
secondCheck = 'Science'
thirdCheck = 'testowanie string'

stringListOnly.append(firstCheck)
stringListOnly.append(secondCheck)
stringListOnly.append(thirdCheck)


stringListOnly.display()