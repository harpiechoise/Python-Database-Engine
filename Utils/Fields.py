def type_stringify(dataType):
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
    def __init__(self,
                 name: any = None,
                 instance: any = type(None)):
        self._instance = instance
        self.name = name

    @staticmethod
    def _make_err_msg(value, instance):
        instance = type_stringify(instance)
        value = type_stringify(type(value))
        return ("Cannot assing a {} ".format(value) +
                " to an {} reference".format(instance).strip())

    @property
    def name(self):
        return self._value

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            raise TypeError(f"String expected but got:" +
                            f"{self._make_err_msg(value)}")

    def __str__(self):
        return str(self.value)


class CharField(BaseField):
    def __init__(self, name: str, maxlen: int):
        super().__init__(name, str)
        self.maxlen = maxlen
        self._value = None

    @property
    def value(self):
        return self._value

    @property
    def maxlen(self):
        return self._maxlen

    @maxlen.setter
    def maxlen(self, maxlen):
        if isinstance(maxlen, int):
            self._maxlen = maxlen
        else:
            raise TypeError(self._make_err_msg(maxlen, int))

    @value.setter
    def value(self, value):
        if isinstance(value, str) and\
           self._max_len_checker(value, self.maxlen):
            self._value = value
        else:
            raise TypeError(self._make_err_msg(value, self._instance))

    def __repr__(self):
        return f"<CharField value={self.value}, maxlen={self.maxlen}>"

    def __len__(self):
        return len(self.value)

    def __eq__(self, other):
        if isinstance(value, str):
            return self.value == other
        elif isinstance(value, type(self)):
            return self.value == other.value
        else:
            raise TypeError("Cannot use the \"==\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __ne__(self, other):
        if isinstance(value, str):
            return self.value != other
        elif isinstance(value, type(self)):
            return self.value != other.value
        else:
            raise TypeError("Cannot use the \"!=\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __lt__(self, other):
        if isinstance(value, str):
            return len(self.value) < len(other)
        elif isinstance(value, type(self)):
            return len(self.value) < len(other.value)
        else:
            raise TypeError("Cannot use the \"<\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __gt__(self, other):
        if isinstance(value, str):
            return len(self.value) > len(other)
        elif isinstance(value, type(self)):
            return len(self.value) > len(other.value)
        else:
            raise TypeError("Cannot use the \">\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __le__(self, other):
        if isinstance(other, str):
            return len(self.value) <= len(other)
        elif isinstance(value, type(self)):
            return len(self.value) <= len(other.value)
        else:
            raise TypeError("Cannot use the \"<=\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __ge__(self, other):
        if isinstance(other, str):
            return len(self.value) <= len(other)
        elif isinstance(value, type(self)):
            return len(self.value) <= len(other.value)
        else:
            raise TypeError("Cannot use the \">=\" operator with types:" +
                            f"{type_stringify(type(self))}" +
                            f"{type_stringify(type(other))}")

    def __add__(self, other):
        if isinstance(value, str):
            return self.value + other
        elif isinstance(value, type(self)):
            return self.value + other.value
        else:
            raise TypeError("Cannot use the \"+\" operator with types:" +
                            f"{type_stringify(self)} {type_stringify(other)}")

    def __sub__(self, other):
        raise TypeError("Cannot use the \"-\" operator with types:" +
                        f"{type_stringify(self)} {type_stringify(other)}")

    def __mul__(self, other):
        if isinstance(other, int):
            return self.value * other
        else:
            raise TypeError("Expected an Integer but recibed an {}"
                            .format(type_stringify(other)))

    def __div__(self, other):
        raise TypeError("Cannot use the \"/\" operator with types:" +
                        f"{type_stringify(self)} {type_stringify(other)}")

    def __floordiv__(self, other):
        raise TypeError("Cannot use the \"//\" operator with types:" +
                        f"{type_stringify(self)} {type_stringify(other)}")

    def __mod__(self, other):
        raise TypeError("Cannot use the \"//\" operator with types:" +
                        f"{type_stringify(self)} {type_stringify(other)}")

    def __pow__(self, other):
        raise TypeError("Cannot use the \"**\" operator with types:" +
                        f"{type_stringify(self)} {type_stringify(other)}")

    @staticmethod
    def _max_len_checker(value, maxlen):
        if len(value) > maxlen:
            raise AssertionError(f"Cannot fit a string of length: " +
                                 f"{len(value)} in a fixed length of {maxlen}")


class PositiveIntegerField(BaseField):
    def __init__(self, value):
        self._instance = int
        self.value = value

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
    x = CharField(name="Yo", maxlen=1)
    x.value = "Jaime"
