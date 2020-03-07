def type_stringify(dataType: any) -> str:
    ''''
    type_stringify:
        This is an utility for exception handling
        this function allows to raise pretty exceptions

    Arguments
    ---------
    datatype
        Is a variable of any Kind this function will
        evaluate the type of this value and return a
        pretty formatted string
    ''''

    dataType = type(dataType)
    if str(dataType) == "<class 'str'>":
        return "String"
    elif str(dataType) == "<class 'NoneType'>":
        return "NoneType"
    elif str(dataType) == "<class 'int'>":
        return "Integer"
    elif str(dataType) == "<class 'float'>":
        return "Float"
    elif str(dataType) == "<class 'complex'>":
        return "Complex"
    elif str(dataType) == "<class 'list'>":
        return "List"
    elif str(dataType) == "<class 'object'>":
        return "Object"
    elif str(dataType) == "<class 'bytes'>":
        return "Bytes"
    elif str(dataType) == "<class 'bytearray'>":
        return "ByteArray"
    elif str(dataType) == "<class 'memoryview'>":
        return "MemoryView"
    elif str(dataType) == "<class 'tuple'>":
        return "Tuple"
    elif str(dataType) == "<class 'dict'>":
        return "Dictionary"
    elif str(dataType) == "<class 'set'>":
        return "Set"
    elif str(dataType) == "<class 'frozenset'>":
        return "FrozeSet"
    elif str(dataType) == "<class 'bool'>":
        return "Boolean"


class BaseField():
    ''''
    BaseField Class
        This class is the base to build fields that node
        and DBManager can handle, this contain all the
        global methods and values for all Field subclasses
        by having field clases gives more control to build
        the final JSON String

    Attributes
    ----------
        private instance: any
            This allows the Database Manager have a strict
            typing, Python is dinamicly Typed, but for the
            dbcompiler needs strict typing to works properly
        public name: str
            This is the name of the field, all fields have a name
            this name is used for build the main JSON, the values
            of the JSON have this format:
                <field_name>:<field_value>
    Methods
    -------
        private static _make_err_msg(value: any, instance: dataType)
            this builds an pretty default error message for the TypeError
            all the types in the fields are fixed and strongly typed,
            when I want to make an CharField for example, I want to allow
            String DataTypes only as values

    Raises
    ------
        TypeError
            When the DataType of the value missmatch with the value of
            the instance, an TypeError will be raised.
    ''''
    def __init__(self,
                 name: any = None,
                 instance: any = type(None)):
        self._instance = instance
        self.name = name

    @staticmethod
    def _make_err_msg(value, instance) -> str:
        instance = type_stringify(instance)
        value = type_stringify(type(value))
        return ("Cannot assing a {} ".format(value) +
                " to an {} reference".format(instance).strip())

    @property
    def name(self) -> str:
        return self._value

    @name.setter
    def name(self, value: str):
        if isinstance(value, str):
            self._value = value
        else:
            raise TypeError(f"String expected but got:" +
                            f"{self._make_err_msg(value)}")

    def __str__(self) -> str:
        return str(self.value)


class CharField(BaseField):
    ''''
    Charfield Class
        This is the String Datatype of the DBEngine
        this fields gives the nodes the capability
        of have a strong typing above Python dinamic
        Typing.

    Attributes
    ----------
        private instance: any
            This allows the Database Manager have a strict
            typing, Python is dinamicly Typed, but for the
            dbcompiler needs strict typing to works properly

        public name: str
            This is the name of the field, all fields have a name
            this name is used for build the main JSON, the values
            of the JSON have this format:
                <field_name>:<field_value>
        public value: str
            This is the value of this CharField, in this case
            only admits string type values

        public maxlen: int
            This limits the length of a String

    Methods
    -------
        private static _make_err_msg(value: any, instance: dataType)
            this builds an pretty default error message for the TypeError
            all the types in the fields are fixed and strongly typed,
            when I want to make an CharField for example, I want to allow
            String DataTypes only as values

    Raises
    ------
        TypeError
            When the DataType of the value missmatch with the value of
            the instance, an TypeError will be raised.

    Capabilities
    ------------
        The most of the strings methods are compatible with this node Type
            - Most of operators
            - Most of built-in Methods

        The equality Method is implemented for search purposes
    ''''
    def __init__(self, name: str, maxlen: int):
        super().__init__(name, str)
        self.maxlen = maxlen
        self._value = None

    @property
    def value(self) -> str:
        return self._value

    @property
    def maxlen(self) -> int:
        return self._maxlen

    @maxlen.setter
    def maxlen(self, maxlen: int):
        if isinstance(maxlen, int):
            self._maxlen = maxlen
        else:
            raise TypeError(self._make_err_msg(maxlen, int))

    @value.setter
    def value(self, value: str):
        if isinstance(value, str) and\
           self._max_len_checker(value, self.maxlen):
            self._value = value
        else:
            raise TypeError(self._make_err_msg(value, self._instance))

    def __repr__(self) -> str:
        return (f"<CharField value={self.value}, maxlen={self.maxlen}" +
                f"at {hex(id(self))}>")

    def __len__(self) -> int:
        return len(self.value)

    def __eq__(self, other: str) -> bool:
        if isinstance(value, str):
            return self.value == other
        elif isinstance(value, type(self)):
            return self.value == other.value
        else:
            raise TypeError("Cannot use the \"==\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __ne__(self, other: str) -> bool:
        if isinstance(value, str):
            return self.value != other
        elif isinstance(value, type(self)):
            return self.value != other.value
        else:
            raise TypeError("Cannot use the \"!=\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __lt__(self, other: str) -> bool:
        if isinstance(value, str):
            return len(self.value) < len(other)
        elif isinstance(value, type(self)):
            return len(self.value) < len(other.value)
        else:
            raise TypeError("Cannot use the \"<\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __gt__(self, other: str) -> bool:
        if isinstance(value, str):
            return len(self.value) > len(other)
        elif isinstance(value, type(self)):
            return len(self.value) > len(other.value)
        else:
            raise TypeError("Cannot use the \">\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __le__(self, other: str) -> bool:
        if isinstance(other, str):
            return len(self.value) <= len(other)
        elif isinstance(value, type(self)):
            return len(self.value) <= len(other.value)
        else:
            raise TypeError("Cannot use the \"<=\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __ge__(self, other: str) -> bool:
        if isinstance(other, str):
            return len(self.value) <= len(other)
        elif isinstance(value, type(self)):
            return len(self.value) <= len(other.value)
        else:
            raise TypeError("Cannot use the \">=\" operator with types:" +
                            f"{type_stringify(type(self))}" +
                            f"{type_stringify(type(other))}")

    def __add__(self, other: str) -> str:
        if isinstance(value, str):
            return self.value + other
        elif isinstance(value, type(self)):
            return self.value + other.value
        else:
            raise TypeError("Cannot use the \"+\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __sub__(self, other: int) -> bool:
        raise TypeError("Cannot use the \"-\" operator with types:" +
                        f"{type_stringify(self)} {type_stringify(other)}")

    def __mul__(self, other: int) -> bool:
        if isinstance(other, int):
            return self.value * other
        else:
            raise TypeError("Expected an Integer but recibed an {}"
                            .format(type_stringify(other)))

    def __div__(self, other: int) -> NotImplemented:
        raise TypeError("Cannot use the \"/\" operator with types:" +
                        f"{type_stringify(self)} {type_stringify(other)}")

    def __floordiv__(self, other: int) -> NotImplemented:
        raise TypeError("Cannot use the \"//\" operator with types:" +
                        f"{type_stringify(self)} {type_stringify(other)}")

    def __mod__(self, other: int) -> NotImplemented:
        raise TypeError("Cannot use the \"//\" operator with types:" +
                        f"{type_stringify(self)} {type_stringify(other)}")

    def __pow__(self, other: int) -> NotImplemented:
        raise TypeError("Cannot use the \"**\" operator with types:" +
                        f"{type_stringify(self)} {type_stringify(other)}")

    @staticmethod
    def _max_len_checker(value: str, maxlen: int):
        if len(value) > maxlen:
            raise AssertionError(f"Cannot fit a string of length: " +
                                 f"{len(value)} in a fixed length of {maxlen}")


class PositiveIntegerField(BaseField):
    def __init__(self, name, instance):
        super().__init__(name, instance)
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, self._instance):
            self._value = value
        else:
            raise TypeError(self._make_err_msg(value, self._instance))


if __name__ == "__main__":
    pass
