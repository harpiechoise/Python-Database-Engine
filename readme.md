# PreAlpha a Python Simple Database Engine

## Developer Documentation

### Description

A simple excercise of a simple database engine implementation. My vision about this project, is make an Database Engine taking concepts of a classic relational databases and also the concept of simplicity of mongodb with his document based database engine, in this way we can take the major advantage of this 2 main concepts, this is a work in progress yet, but, at the near future I plan to have the core of this project to lead the major development of this open source project for the general comunity.

### What's done now?

At this point I have done 2 main data fields staticly typed, unlike python, this fields only accepts an specific format and type of data, this brings more control for the user and the future Database Language Server, the fields currently implemented are specified in the next seccion of this document.

A Table Class, this table that is currently in charge:
    - Be a representation of data
    - Make a Collection Structure of the data
    - Save the data

This Table Class is based in the Single Linked List Data Structure, With nodes that represents an element which cotains the data of the table, this feature brings performance for search data, and more control to save and load the database.

The DataNode, this node is the base information container, and the main DataType for the Table, this DataType allows the auto primary_key assignation, and auto increments, The primary keys are unasignable, because the primary key is the only information thats be loaded from __.jcdb__ files, in this way we don't need to have all the data of the database loaded in the memory in rutime, this means performance, when you want to perform a search, the DataNode will able to grab a piece of data from the __.jcdb file__ only from an index.

This feature is made possible by the structure of the __jcdb file__, the data is directly asociated to a index, and not to a name or key, and when the data is deleted the index is deleted to, by this way the program don't have to load ghost indexes.

### TODO NOW
- Class Documentation: This is the current WIP
- Load mechanism: A way to load only the indexes from memory, and when we pass a certain index to a data node, this be able to load the data from the __.jcdb__ file.
- Search Mechanism: A way to search data traversing the linked list in search of certain value.
- BaseField Required Mechanism: A way to have optional values for all the fields who inherit from BaseField Class
- DataNode Load Mechanism: A way to retrieve the data from a field back to DataNode by passing and index to the __init__ class

### Data Fields
- CharField: Is the String Type of the database, the Charfield Type can holds ONLY String values, in addition to this, CharField haves a lot of the Common Methods of the strings in python, the allowed Methods on Charfields are the next:

    - Concatenation
    - Comparison
    - Len
    - Greater Than
    - Less Than
    - Greater or equals Than
    - Less or equals Than
    - String Repeat

    - Example:

        ~~~python
            # IN
            c1 = CharField("Saludo", 4)
            c1.value = "Hola"
            c2 = CharField("Saludo2", 4)
            c2.value = "Hola"
            c3 = CharField("Saludo3", 17)
            c3.value = "¿Hola Como Estas?"
            print("C1:", c1)
            print("C2:", c2)
            print("C3:", c3)
            print("¿Es igual C1 a C2?:", c1 == c2)
            print("¿Es igual C1 a C3?:", c1 == c3)
            print("¿Es mas grande C1 a C3?:", c1 > c3)
            print("¿Mas pequeña?:", c1 < c3)
            print("¿Longitud de C3?:", len(c3))
            print("¿Concatenadas?:", c1 + " " + c3)
            print("¿C1 * 4?:", c1 * 4)

            # C1: Hola
            # C2: Hola
            # C3: ¿Hola Como Estas?
            # ¿Es igual C1 a C2?: True
            # ¿Es igual C1 a C3?: False
            # ¿Es mas grande C1 a C3?: False
            # ¿Mas pequeña?: True
            # ¿Longitud de C3?: 17
            # ¿Concatenadas?: Hola ¿Hola Como Estas?
            # ¿C1 * 4?: HolaHolaHolaHola
        ~~~~

- IntegerField: Is the Integer Type of the database, the Integer Type can holds ONLY Integer values, in addition to this, Integer haves a lot of the Common Methods of the integers in Python, the allowed Methods on Charfields are the next:
  - Equality
  - Greater Than
  - Less Than
  - Greater or equals Than
  - Less or equals Than
  - Addition
  - Subtaction
  - Multiplication
  - Division
  - Floor Division
  - Power
  - Left Shift
  - Right Shift
  - Logical Or
  - Invertion
  - Xor
  - Logical And
  
  - Example:
   ~~~python
    print("N1", n1)
    print("N2", n2)
    print("N3", n3)
    print("N4", n4)
    print("¿Es igual N1 a N2?:", n1 == n2)
    print("¿Es igual N1 a N3?:", n1 == n3)
    print("¿Es mas grande N1 a N3?:", n1 > n3)
    print("¿Mas pequeño?:", n1 < n3)
    print("¿Es mas mayor o igual N1 a N2?:", n1 >= n2)
    print("Es Menor o Igual N1 a N3", n1 <= n3)
    print("Suma N1 + N3:", n1 + n3)
    print("Resta N1 - N3:", n1 - n3)
    print("Division N3 / N1:", n3 / n1)
    print("DivFloor N1 // N3:", n1 // n3)
    print("Exponenciacion N3 ** N1:", n3 ** n1)
    print("Left Shift N3 << N1:", n3 << n1)
    print("Rigth Shift N3 >> N1:", n3 >> n1)
    print("~N1:", ~n1)
    print("+N1:", +n1)
    print("-N1:", -n1)
    print("+N4:", +n4)
    print("-N4:", -n4)
    print("N1 | N2", n1 | n2)
    # OUT
    # ¿Es igual N1 a N2?: True
    # ¿Es igual N1 a N3?: False
    # ¿Es mas grande N1 a N3?: True
    # ¿Mas pequeño?: False
    # ¿Es mas mayor o igual N1 a N2?: True
    # Es Menor o Igual N1 a N3 False
    # Suma N1 + N3: 30
    # Resta N1 - N3: 10
    # Division N3 / N1: 0.5
    # DivFloor N1 // N3: 2
    # Exponenciacion N3 ** N1: 100000000000000000000
    # Left Shift N3 << N1: 10485760
    # Rigth Shift N3 >> N1: 0
    ~~~

# Usage 

~~~bash
git clone <clone_url>
# There is only one dependency for now
pip install -r requeriments.txt
#OR
pip install tabulate==0.8.6
~~~

**This is actually only for developing use**

~~~python
from Schema.Table import Table
from Utils.Fields import *


class Client(Table):
    def __init__(self):
        # fields declaration first
        self.client_name = CharField(name="Client Name", maxlen=20)
        self.age = IntegerField(name="Age")
        super().__init__(table_name="Client_Data")


if __name__ == "__main__":
    a = Client()
    a.client_name.value = "Tommy"
    a.age.value = 21
    a.save()
    a.client_name.value = "Josh"
    a.age.value = 60
    a.save()
    a.client_name.value = "Norma"
    a.age.value = 40
    a.save()
    a.client_name.value = "Lenny"
    a.age.value = 25
    a.save()
    a.client_name.value = "Mr. Burns"
    a.age.value = 1500
    a.save()
    a.migrate()
~~~

The resulting file of this code is the following:

~~~json
{
	"0": {
		"client_name": "Tommy",
		"age": 21
	},
	"1": {
		"client_name": "Josh",
		"age": 60
	},
	"2": {
		"client_name": "Norma",
		"age": 40
	},
	"3": {
		"client_name": "Lenny",
		"age": 25
	},
	"4": {
		"client_name": "Mr. Burns",
		"age": 1500
	}
}

~~~

## Explanation 

To create a table you have to inherits from Table class to a subclass containing the fields name, to this name we binds the FieldType and at the end with call the init method of the super class, this allows to the superclass to parse all the fields to make a internal summary of the table itself, finally we assing the name of the table name in the \_\_init\_\_ method of the Table super class.


~~~python
class Client(Table):
    def __init__(self):
        # fields declaration first
        self.client_name = CharField(name="Client Name", maxlen=20)
        self.age = IntegerField(name="Age")
        super().__init__(table_name="Client_Data")
~~~

### Diference between save and migrate

The save method save the data into a node, and includes him to a LinkedList, and migrate builds the json schema and save to a file.

### Misc Methods
`Schema.Table.summary(self)`: Is an utility for the future language server, this allow to print a summary of the table itself
Usage:

~~~python
print(a.summary())

# OUT

# Name         Value
# -----------  ----------------------------------------
# client_name  Charfield(@name=Client Name, @maxlen=20)
# age          IntegerField(@name=Age)
~~~

This document will be updated at the end of an iteration.
