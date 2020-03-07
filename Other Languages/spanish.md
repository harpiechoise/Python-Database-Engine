# PreAlpha un Motor simple de Base de Datos
 
## Documentación para desarrollador
 
### Descripción
 
Este es un ejercicio de un motor de base de datos simple. Mi vision de este proyecto, es hacer un motor de base de datos tomando conceptos de las bases de datos relacionales, y tambien el concepto de simplicidad de mongodb y su motor de base de datos orientado a documentos, de esta manera podemos tomar ventaja de estos dos conceptos principales, este trabajo aún está en progreso, pero, hacia el futuro cercano planeo tener el núcleo del proyecto para conducir al desarrollo más pesado de este proyecto open source para la comunidad en general
 
### ¿Que está hecho hasta ahora?
 
En este punto del desarrollo tengo 2 campos de datos de tipado estático, a diferencia de Python estos campos aceptan un formato especifico de datos, esto nos ofrece mas control para el usuario y para el futuro Database Language server, estos campos actualmente implementados estan en la siguiente sección de este documento.
 
Ademas de los campos, tengo un Table Class, que actualmente esta encargada de las siguientes tareas:
   - Ser una representación de los datos
   - Crear la estructura de datos basada en Diccionarios
   - Guardar los datos
 
Esta Table Class esta basada en la estructura de datos "Single Linked List", con nodos que representan el elemento principal que contiene los datos de la table, esta característica se traduce en rendimiento al momento de buscar datos, y más control al momento de cargar y guardar la base de datos
 
La clase DataNode, es el contenedor base para toda la información de la tabla, y el tipo de datos principal para la Table, este tipo de datos nos permite asignar las llaves primarias de forma automática, y auto incrementarla, las llaves primarias son inasignables, porque la llave primaria es la unica información que va a ser cargada desde los archivos __.jcdb__ hacia la memoria ram, de esta no necesitamos todos los datos para realizar una búsqueda y tampoco necesitamos que todos los datos estén cargados en la memoria mientras el programa esta corriendo, esto se traduce en rendimiento, cuando quieras realizar una búsqueda, el Datanode va a ser capaz de tomar una pieza de los datos a partir de un indice.
 
Esta caracteristica es posible por la estructura de los archivos __jcdb__, los datos estan directamente asociados con los indices, y no a un nombre o a un llave, y cuando se borra un valor el indice tambien es borrado, de esa manera evitamos lidiar con indices fantasma
 
### ¿Que hay por hacer ahora?
__(Seguda iteracion)__
- Documentación de las clases: Esto es en lo que estoy trabajando actualmente
- Mecanismo para cargar los datos: Una manera de cargar solo los indices en del archivo __.jcdb__ dentro de la memoria RAM.
- Mecanismo de búsqueda: Una manera de buscar datos atravesando la lista enlazada buscando un valor en particular
- Mecanismo de campo requerido: Tener una manera de hacer valores opcionales para todos los campos que hereden de la clase BaseField.
- Mecanismo para cargar los datos hacia el DataNode: Una manera de recuperar los datos a partir de un indice.
 
 
### DataFields
- CharField: Es un campo que acepta valores de tipo String, el Charfield solo puede contener valores de tipo String, en adición a esto, el CharField tiene muchos de los métodos comunes de las cadenas en Python, los métodos permitidos por este tipo de dato son:
   - Concatenación
   - Comparación
   - Len()
   - Mayor Que
   - Menor Que
   - Mayor o igual que
   - Menor o igual que
   - Repetición de cadenas
 
   - Ejemplo:
 
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
- IntegerField: Es un campo que acepta valores de tipo Entero, el Charfield solo puede contener valores de tipo Entero, en adicion a esto, el CharField tiene muchos de los métodos comunes de los enteros en Python, los métodos permitidos por este tipo de dato son:
 - Igualdad
 - Mayor Que
 - Menor Que
 - Mayor o igual que
 - Menor o igual que
 - Adicion
 - Sustaccion
 - Multiplicacion
 - Division
 - Floor Division
 - Exponenciacion
 - Left Shift
 - Right Shift
 - O Logico
 - Inversion
 - O Exclusivo
 - & Logico
 
 - Ejemplo:
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
 
# Uso de la libreria
~~~bash
git clone <clone_url>
# Aqui solo hay una dependecia actualmente
pip install -r requeriments.txt
# O
pip install tabulate==0.8.6
~~~
 
**Actalmente esta libreria es de uso exclusivo para desarroladores**
 
Python
From Schema.Table import Table
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
 
El archivo resultante del codigo anterior es el siguiente:
 
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
 
## Explicación
 
Para crear una table debes heredar desde la clase Tabla y la subclase es la que contiene los campos, esto es para que la superclase Tabla pueda leer los campos agregados por la persona que está usando la librería, finalmente se debe llamar al método \_\_init\_\_ de la superclase Tabla, y con estos nombres la superclase va a hacer resúmenes internos con el fin de ayudar al futuro usuario final cuando este ocupando el lenguaje del motor de base de datos
 
~~~python
class Client(Table):
   def __init__(self):
       # fields declaration first
       self.client_name = CharField(name="Client Name", maxlen=20)
       self.age = IntegerField(name="Age")
       super().__init__(table_name="Client_Data")
~~~
 
 
### Diferencias entre Save y Migrate
 
El método save, guarda los datos dentro de un nodo y los incluye dentro del linked list, y el método migrate construye el esquema interno en Json y lo guarda a un archivo.
 
### Metodos Miscelaneos
`Schema.Table.Summary(self)`: Es una utilidad para el futuro servidor del lenguaje de l abase de datos se sirve para mostrar un resumen de la tabla en si misma.
 
~~~python
print(a.summary())
 
# OUT
 
# Name         Value
# -----------  ----------------------------------------
# client_name  Charfield(@name=Client Name, @maxlen=20)
# age          IntegerField(@name=Age)
~~~
 
Este documento va a ser actualizado al fin de cada iteración
