def type_stringify(dataType: any, is_type: bool = False) -> str:
    '''
    type_stringify:
        This is an utility for exception handling
        this function allows to raise pretty exceptions

    Arguments
    ---------
    datatype
        Is a variable of any Kind this function will
        evaluate the type of this value and return a
        pretty formatted string
    '''

    if not is_type:
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
    '''
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
    '''
    def __init__(self,
                 name: str = None,
                 instance: any = type(None)):
        # The strict Datatype Allowed
        # For this node Type
        self._instance = instance
        # The name of the field
        self.name = name

    @staticmethod
    def _make_err_msg(value, instance) -> str:
        # And utility for generate the most common err message
        instance = type_stringify(instance, is_type=True)
        value = type_stringify(value)
        return ("Cannot assing a {} ".format(value) +
                " to an {} reference".format(instance).strip())

    @property
    def name(self) -> str:
        return self._value

    @name.setter
    def name(self, value: str):
        # Type Strict
        if isinstance(value, str):
            self._value = value
        else:
            raise TypeError(f"String expected but got:" +
                            f"{self._make_err_msg(value)}")

    # The string Representation
    def __str__(self) -> str:
        return str(self.value)


class CharField(BaseField):
    '''
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
    '''

    def __init__(self, name: str, maxlen: int):
        super().__init__(name, str)
        self.maxlen = maxlen

    @property
    def value(self) -> str:
        return self._value

    @property
    def maxlen(self) -> int:
        return self._maxlen

    @maxlen.setter
    def maxlen(self, maxlen: int):
        if maxlen <= 0:
            raise AssertionError("Lenght cannot be negative or zero")
        if isinstance(maxlen, int):
            self._maxlen = maxlen
        else:
            raise TypeError(self._make_err_msg(maxlen, int))

    @value.setter
    def value(self, value):
        # Type Strict
        if isinstance(value, self._instance) and\
           self._max_len_checker(value, self.maxlen):
            self._value = value
        else:
            raise TypeError(self._make_err_msg(value, self._instance))

    def _type_name(self):
        # A representation for the summary
        return f"Charfield(@name={self.name}, @maxlen={self.maxlen})"

    # DUNDER
    # DUNDER
    # DUNDEEEER
    # https://docs.python.org/3/reference/datamodel.html
    def __repr__(self) -> str:
        return (f"<CharField value={self.value}, maxlen={self.maxlen}" +
                f" at {hex(id(self))}>")

    def __len__(self) -> int:
        return len(self.value)

    def __eq__(self, other: str) -> bool:
        if isinstance(other, self._instance):
            return self.value == other
        elif isinstance(other, type(self)):
            return self.value == other.value
        else:
            raise TypeError("Cannot use the \"==\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __ne__(self, other: str) -> bool:
        if isinstance(other, self._instance):
            return self.value != other
        elif isinstance(other, type(self)):
            return self.value != other.value
        else:
            raise TypeError("Cannot use the \"!=\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __lt__(self, other: str) -> bool:
        if isinstance(other, str):
            return len(self.value) < len(other)
        elif isinstance(other, type(self)):
            return len(self.value) < len(other.value)
        else:
            raise TypeError("Cannot use the \"<\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __gt__(self, other: str) -> bool:
        if isinstance(other, str):
            return len(self.value) > len(other)
        elif isinstance(other, type(self)):
            return len(self.value) > len(other.value)
        else:
            raise TypeError("Cannot use the \">\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __le__(self, other: str) -> bool:
        if isinstance(other, str):
            return len(self.value) <= len(other)
        elif isinstance(other, type(self)):
            return len(self.value) <= len(other.value)
        else:
            raise TypeError("Cannot use the \"<=\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __ge__(self, other: str) -> bool:
        if isinstance(other, str):
            return len(self.value) >= len(other)
        elif isinstance(other, type(self)):
            return len(self.value) >= len(other.value)
        else:
            raise TypeError("Cannot use the \">=\" operator with types:" +
                            f"{type_stringify(self)}" +
                            f"{type_stringify(other)}")

    def __add__(self, other: str) -> str:
        if isinstance(other, self._instance):
            return self.value + other
        elif isinstance(other, type(self)):
            return self.value + other.value
        else:
            raise TypeError("Cannot use the \"+\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __radd__(self, other: str) -> str:
        if isinstance(other, self._instance):
            return other + self.value
        elif isinstance(other, type(self)):
            return other.value + self.value
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

    def __rmul__(self, other: int) -> bool:
        if isinstance(other, int):
            return other * self.value
        else:
            raise TypeError("Expected an Integer but recibed an {}"
                            .format(type_stringify(other)))

    def __len__(self) -> int:
        return len(self.value)

    def __eq__(self, other: str) -> bool:
        if isinstance(other, self._instance):
            return self.value == other
        elif isinstance(other, type(self)):
            return self.value == other.value
        else:
            raise TypeError("Cannot use the \"=name=\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __ne__(self, other: str) -> bool:
        if isinstance(other, self._instance):
            return self.value != other
        elif isinstance(other, type(self)):
            return self.value != other.value
        else:
            raise TypeError("Cannot use the \"!=\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __lt__(self, other: str) -> bool:
        if isinstance(other, self._instance):
            return len(self.value) < len(other)
        elif isinstance(other, type(self)):
            return len(self.value) < len(other.value)
        else:
            raise TypeError("Cannot use the \"<\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __gt__(self, other: str) -> bool:
        if isinstance(other, self._instance):
            return len(self.value) > len(other)
        elif isinstance(other, type(self)):
            return len(self.value) > len(other.value)
        else:
            raise TypeError("Cannot use the \">\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __add__(self, other: str) -> str:
        if isinstance(other, self._instance):
            return self.value + other
        elif isinstance(other, type(self)):
            return self.value + other.value
        else:
            raise TypeError("Cannot use the \"+\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __sub__(self, other: int) -> bool:
        raise TypeError("Cannot use the \"-\" operator with types:" +
                        f"{type_stringify(self)} {type_stringify(other)}")

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
            return None
        else:
            return True


class IntegerField(BaseField):
    '''
    IntegerField
        This is the Base Type for all Integer Fields

    Attributes
    ----------
        name
            Is the name of the field for the creation is for
            the json Creation following the structure
                <self.name>:<value>
        value
            Is the value of the field

        capabilities
            All the capabilities of native Python Integer Type
    '''
    def __init__(self, name):
        super().__init__(name, int)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        # Type Strict ;-;
        if isinstance(value, self._instance):
            self._value = value
        else:
            raise TypeError(self._make_err_msg(value, self._instance))
    # DUNDER
    # DUNDER
    # DUNDEEEER
    # https://docs.python.org/3/reference/datamodel.html

    def _type_name(self):
        return f"IntegerField(@name={self.name})"

    def __eq__(self, other: int) -> bool:
        if isinstance(other, self._instance):
            return self.value == other

    def __le__(self, other: str) -> bool:
        if isinstance(other, self._instance):
            return len(self.value) <= len(other)
        elif isinstance(other, type(self)):
            return len(self.value) <= len(other.value)
        else:
            raise TypeError("Cannot use the \"<=\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")
            raise TypeError("Cannot use the \"=name=\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __ne__(self, other: int) -> bool:
        if isinstance(other, self._instance):
            return self.value != other
        elif isinstance(other, type(self)):
            return self.value != other.value
        else:
            raise TypeError("Cannot use the \"!=\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __lt__(self, other: int) -> bool:
        if isinstance(other, self._instance):
            return self.value < other
        elif isinstance(other, type(self)):
            return self.value < other.value
        else:
            raise TypeError("Cannot use the \"<\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __gt__(self, other: int) -> bool:
        if isinstance(other, self._instance):
            return self.value > other
        elif isinstance(other, type(self)):
            return self.value > other.value
        else:
            raise TypeError("Cannot use the \">\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __le__(self, other: int) -> bool:
        if isinstance(other, self._instance):
            return self.value <= other
        elif isinstance(other, type(self)):
            return self.value <= other.value
        else:
            raise TypeError("Cannot use the \"<=\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __ge__(self, other: int) -> bool:
        if isinstance(other, self._instance):
            return self.value <= other
        elif isinstance(other, type(self)):
            return self.value <= other.value
        else:
            raise TypeError("Cannot use the \">=\" operator with types:" +
                            f"{type_stringify(type(self))}" +
                            f"{type_stringify(type(other))}")

    def __add__(self, other):
        if isinstance(other, self._instance):
            return self.value + other
        elif isinstance(other, type(self)):
            return self.value + other.value
        else:
            raise TypeError("Cannot use the \"+\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __sub__(self, other):
        if isinstance(other, self._instance):
            return self.value - other
        elif isinstance(other, type(self)):
            return self.value - other.value
        else:
            raise TypeError("Cannot use the \"-\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __mult__(self, other):
        if isinstance(other, self._instance):
            return self.value * other
        elif isinstance(other, type(self)):
            return self.value * other.value
        else:
            raise TypeError("Cannot use the \"*\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __truediv__(self, other):
        if isinstance(other, self._instance):
            return self.value / other
        elif isinstance(other, type(self)):
            return self.value / other.value
        else:
            raise TypeError("Cannot use the \"/\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __floordiv__(self, other):
        if isinstance(other, self._instance):
            return self.value // other
        elif isinstance(other, type(self)):
            return self.value // other.value
        else:
            raise TypeError("Cannot use the \"//\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __mod__(self, other):
        if isinstance(other, self._instance):
            return self.value % other
        elif isinstance(other, type(self)):
            return self.value % other.value
        else:
            raise TypeError("Cannot use the \"%\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __divmod__(self, other):
        if isinstance(other, self._instance):
            return divmod(self.value, other)
        elif isinstance(self.value, type(self)):
            return divmod(self.value, other.value)
        else:
            raise TypeError("Cannot use the \"divmod\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __pow__(self, other):
        if isinstance(other, self._instance):
            return self.value ** other
        elif isinstance(other, type(self)):
            return self.value ** other.value
        else:
            raise TypeError("Cannot use the \"**\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __radd__(self, other):
        if isinstance(other, self._instance):
            return other + self.value
        elif isinstance(other, type(self)):
            return other.value + self.value
        else:
            raise TypeError("Cannot use the \"+\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __rsub__(self, other):
        if isinstance(other, self._instance):
            return other - self.value
        elif isinstance(other, type(self)):
            return other.value - self.value
        else:
            raise TypeError("Cannot use the \"-\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __rmult__(self, other):
        if isinstance(other, self._instance):
            return other * self.value
        elif isinstance(other, type(self)):
            return other.value * self.value
        else:
            raise TypeError("Cannot use the \"*\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __rtruediv__(self, other):
        if isinstance(other, self._instance):
            return other / self.value
        elif isinstance(other, type(self)):
            return other.value / self.value
        else:
            raise TypeError("Cannot use the \"/\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __rfloordiv__(self, other):
        if isinstance(other, self._instance):
            return other // self.value
        elif isinstance(other, type(self)):
            return other.value // self.value
        else:
            raise TypeError("Cannot use the \"//\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __rmod__(self, other):
        if isinstance(other, self._instance):
            return other % self.value
        elif isinstance(other, type(self)):
            return other.value % self.value
        else:
            raise TypeError("Cannot use the \"%\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __rdivmod__(self, other):
        if isinstance(other, self._instance):
            return divmod(other, self.value)
        elif isinstance(value, type(self)):
            return divmod(other.value, self.value)
        else:
            raise TypeError("Cannot use the \"divmod\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __rpow__(self, other):
        if isinstance(other, self._instance):
            return other ** self.value
        elif isinstance(other, type(self)):
            return other.value ** self.value
        else:
            raise TypeError("Cannot use the \"**\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __lshift__(self, other):
        if isinstance(other, self._instance):
            return self.value << other
        elif isinstance(other, type(self)):
            return self.value << other.value
        else:
            raise TypeError("Cannot use the \"<<\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __rshift__(self, other):
        if isinstance(other, self._instance):
            return self.value >> other
        elif isinstance(other, type(self)):
            return self.value >> other.value
        else:
            raise TypeError("Cannot use the \">>\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __pos__(self):
        if self.value < 0:
            return ~self.value + 1
        else:
            return self.value

    def __neg__(self):
        if self.value > 0:
            return ~self.value + 1
        else:
            return self.value

    def __abs__(self):
        if self.value < 0:
            return ~self.value + 1
        else:
            return self.value

    def __invert__(self):
        return ~self.value

    def __and__(self, other):
        if isinstance(other, self._instance):
            return self.value & other
        elif isinstance(other, type(self)):
            return self.value & other.value
        else:
            raise TypeError("Cannot use the \"&\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __or__(self, other):
        if isinstance(self.value, self._instance):
            return self.value | other
        elif isinstance(other, type(self)):
            return self.value | other.value
        else:
            raise TypeError("Cannot use the \"|\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __xor__(self, other):
        if isinstance(self.value, self._instance):
            return self.value ^ other
        elif isinstance(other, type(self)):
            return self.value ^ other.value
        else:
            raise TypeError("Cannot use the \"^\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")
