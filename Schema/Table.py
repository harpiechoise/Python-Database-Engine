from Utils.LinkedLists import BaseList, BaseNode
from Utils.Fields import *
from tabulate import tabulate
import json
import os


class DataNode(BaseNode):
    '''
    DataNode
    --------
        The DataNode is the base DataType of the Table
        DataStructure, this is the data container of a Table
        And helps to keep Tracks of the ID's of the data in the
        main database file.

    Attributes
    ----------
        private node_id : int
            This is the primary key. This primary helps
            to identify and keep track to an specific node
            in the LinkedList DataStructure

        public next_node : BaseNode
            The nodes can have a link to the next node in the list
            This ables to build the LinkedList
        public data: Dict
            This is the dictionary, this holds all the data of the
            database item
    '''
    def __init__(self, data: dict):
        # The dict for hold the data
        self.data = data
        # Self explanatory ?
        self._next_node = None
        # Same ?
        self._node_id = 0

    @property
    def data(self) -> dict:
        return self._data

    @data.setter
    def data(self, data: dict):
        # Types Types and More Types
        if isinstance(data, dict):
            self._data = data
        else:
            return TypeError("Data must be a JSON or Dict")


class Table(BaseList):
    '''
    BaseList
        This is an Single Link LinkedList Data Structure Implementation
        this implementation is the Base for the Double Link LinkedList
        and the base for the table implementation.
        This datastructure is able to traverse the list forward
        but not to traverse backwards or perform a search


        Attributes
        ----------
        public elements : int
            This helps to track the number of elements in the list
            and is returned when apply's the len function
            example:
                len(BaseListInstance) -> elements
        private instance: BaseNode
            It's allows to the class to only be strict when try to
            change the node instances of the list, the instance
            specifies the datatype wich can a LinkedList object
            can handle.
        private genesis: BaseNode
            This is the genesis node, the first node in the list
            when the list is created must have at least one node value

        public name: str
            This value holds the table name, for the creation of
            the .jcdb file

        private structure: dict
            This holds the json generated on in the migration step
            this structure after the generation is saved to a file

        private fields: dict
            This holds the fields metadata for the internal
            summary generation

        private fields_show: dict
            This holds a string representation of the Fields
            objects

        private ready_for_save: bool
            This flags indicates to the save methods if all
            values are ready for saving this plays a major
            role with the optional fields implementation

        Methods
        -------
        del_first_node() -> None:
            This method helps to bypass the setter of the first
            node in the LinkedList
            WARNING: This is for safe destruction porpuses only
            you never delete the first node because the node instances
            will be stay caught in the RAM and may cause a memory leak
        move_forward() -> BaseNode:
            This method traverses the list forward and return the last
            node is the utility for insert a node in the last position
            in the list
        insert_after(node: BaseNode, new_node: BaseNode) -> None
            This method insert the new_node instance after the
            node instance.
        insert_last(node: BaseNode) -> None
            This method insert the node at the finish position of the list
        insert_first(node: BaseNode) -> None
            This method insert the node at the first position of the list
        remove_after(node: BaseNode) -> None
            This removes the node after the node instance of the node parameter
        private get_fields(self) -> None
            This method gets the fields and grab the meta_data for the field
            related class information
        public summary(self) -> str
            This method return a string with a internal table data
            representation.
        private pre_migrate(self) -> None
            This method checks if the fields are ready to save
        private pre_migrate_step_2(self) -> DataNode
            This methods constructs the DataNodes
        private migrate(self) -> None
            This method index all the Nodes and checks if all nodes.
            are part of the table
        private make_structure(self) -> None:
            This method make the json structure to be ready for save
            step
        public save(self) -> None:
            Executes the make_structure methods the main idea is implements
            all the middlewares overriding this class, for data transformation,
            value_checking, and data integrity checks.
        public migrate(self) -> None:
            This checks if the .DB folder exists if not this method creates
            this folder and save the file, the main idea of this method is
            to allow the overriding for middleware excecution.
    '''
    def __init__(self, table_name: str):
        # Super Class initialization
        super().__init__(None)
        # Oh Really?
        self._name: str = table_name
        # .-.
        self._structure: dict = {}
        # (╯°□°）╯︵ ┻━┻
        self._fields: dict, self._fields_show: dict = self._get_fields()
        self._ready_for_save: bool = False

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        # Types （〜^∇^)〜
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("The name of the table must be a String")

    def _get_fields(self) -> (dict, dict):
        fields = {}
        named_fields = {}
        # Nothing complex
        for k in self.__dict__.keys():
            # In this line check's for the first character
            # Or if the elements attribute
            if not k.startswith("_") and k is not "elements":
                # If not
                # You hack Facebook
                fields[k] = self.__dict__[k]
                named_fields[k] = self.__dict__[k]._type_name()
            else:
                # Else continue trying bro.
                continue
        return fields, named_fields

    def summary(self) -> str:
        o = []
        for i in self._fields_show.keys():
            o.append([i, self._fields_show[i]])
        # This makes pretier the summary
        p1 = tabulate(o, headers=["Name", "Value"])

        return "\n\n" + p1 + "\n\n"

    def _pre_migrate(self):
        for k in self._fields:
            if self._fields[k].value:
                # Checking if values are ready
                self._ready_for_save = True
            else:
                self._ready_for_save = False
                break

    def _pre_migrate_step_2(self) -> DataNode:
        self._pre_migrate()
        node_dict = {}
        if self._ready_for_save:
            # If it's values are ready for save
            for k in self._fields.keys():
                # You make the node data
                node_dict[k] = self._fields[k].value
        else:
            raise AssertionError("All values are Required")

        return DataNode(node_dict)

    def _migrate(self):
        if self.elements is 0:
            # Insert the first node in the list
            self.insert_first(self._pre_migrate_step_2())
        else:
            # If the list has a first node the node
            # Is inserted in the last position
            self.insert_last(self._pre_migrate_step_2())
        # Updating Counter 〜(^∇^〜）
        self._count_nodes()

    def _make_structure(self):
        # Excecute the previous step
        self._migrate()
        # Get the first
        node = self.first_node
        while node:
            # Gets all the data
            # For launch a rocket
            self._structure[node.node_id] = node.data
            node = node.next_node

    def save(self):
        # Then you build the rocket
        self._make_structure()

    def migrate(self):
        # And save the file
        # Launch a rocket is so overbudget
        if not os.path.exists(".DB"):
            os.mkdir(".DB")

        with open(f".DB/{self.name}_table.jcdb", "w", encoding="utf8") as f:
            f.write(json.dumps(self._structure))

    def __show_schema(self):
        # Shows the JSON Schema
        # 〜(^∇^〜）
        print(self._structure)


class Cliente(Table):
    def __init__(self):
        self.nombre = CharField(name="Nombre", maxlen=100)
        self.edad = IntegerField(name="Edad")
        super().__init__(table_name="Cliente")
