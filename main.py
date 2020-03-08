from Schema.Table import Table
from Utils.Fields import *


class Client(Table):
    def __init__(self):
        # fields declaration first
        self.client_name = CharField(name="Client Name", maxlen=20)
        self.age = IntegerField(name="Age")
        super().__init__(table_name="Client_Data")


if __name__ == "__main__":
    pass
