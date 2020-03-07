from Utils.LinkedLists import BaseList, BaseNode
from Utils.Fields import *
from tabulate import tabulate
import json
import os


class DataNode(BaseNode):
    def __init__(self, data):
        self.data = data
        self._next_node = None
        self._node_id = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if isinstance(data, dict):
            self._data = data
        else:
            return TypeError("Data must be a JSON or Dict")


class Table(BaseList):
    def __init__(self, table_name):
        super().__init__(None)
        self._name = table_name
        self._structure = {}
        self._nodes = []
        self._fields, self._fields_show = self._get_fields()
        self._ready_for_save = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("The name of the table must be a String")

    def _get_fields(self):
        fields = {}
        named_fields = {}
        for k in self.__dict__.keys():
            if not k.startswith("_") and k is not "elements":
                fields[k] = self.__dict__[k]
                named_fields[k] = self.__dict__[k]._type_name()
            else:
                continue
        return fields, named_fields

    def summary(self):
        o = []
        for i in self._fields_show.keys():
            o.append([i, self._fields_show[i]])
        p1 = tabulate(o,
                      headers=["Name", "Value"])

        return "\n\n" + p1 + "\n\n"

    def _pre_migrate(self):
        for k in self._fields:
            if self._fields[k].value:
                self._ready_for_save = True
            else:
                self._ready_for_save = False
                break

    def _pre_migrate_step_2(self):
        self._pre_migrate()
        node_dict = {}
        if self._ready_for_save:
            for k in self._fields.keys():
                node_dict[k] = self._fields[k].value
        else:
            raise AssertionError("All values are Required")

        return DataNode(node_dict)

    def _migrate(self):
        if self.elements is 0:
            self.insert_first(self._pre_migrate_step_2())
        else:
            self.insert_last(self._pre_migrate_step_2())
        self._count_nodes()

    def _make_structure(self):
        self._migrate()
        node = self.first_node
        while node:
            self._structure[node.node_id] = node.data
            node = node.next_node

    def save(self):
        self._make_structure()

    def migrate(self):
        if not os.path.exists(".DB"):
            os.mkdir(".DB")

        with open(f".DB/{self.name}_table.jcdb", "w", encoding="utf8") as f:
            f.write(json.dumps(self._structure))

    def __show_schema(self):
        print(self._structure)


class Cliente(Table):
    def __init__(self):
        self.nombre = CharField(name="Nombre", maxlen=100)
        self.edad = IntegerField(name="Edad")

        super().__init__(table_name="Cliente")
