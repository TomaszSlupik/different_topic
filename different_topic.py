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
