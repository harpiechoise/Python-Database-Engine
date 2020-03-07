# Mi vision de como deberia ser la estructura básica
# Del motor de Base de Datos
# Estructura a conseguir
# DB.locdb
# Basado en JSON
# [
# <nombre_tabla>: {
#  {
#    <id>: {
#    <campos>:<valores>
#    }
#  }
# }
# ]

# LinkedList ?
# LinkedList Bidireccional se ha dicho

NODE_TYPE_ERROR = TypeError("The linked list only admits Node types objects")
NODE_ASSERT_ERROR = AssertionError("Cannot insert a Node after last node" +
                                   " use insert_last instead.")

# Haciendo la lista enlazada

# Nombre de Tabla -> Valor enlazado 1 -> Valor enlazado 2 ... n


class BaseNode:
    '''
        Base Node Class
        This is a Base DataType of the BaseLinkedList.
        And the base for the implementation of the
        DoubleNode Datatype

        Attributes
        ----------
            private node_id : int:
                This is the primary key. This primary helps
                to identify and keep track to an specific node
                in the LinkedList DataStructure

            public next_node : BaseNode:
                The nodes can have a link to the next node in the list
                This ables to build the LinkedList
    '''

    def __init__(self):
        self._node_id: int = 0  # Genesis
        self._next_node = None
        # self._instance = self

    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, new_id):
        self._node_id = new_id

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node

    def __repr__(self):
        return "BaseNode(NodeId={})".format(self.node_id)


class BaseList:
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

        Raises
        ------
        AssertionError:
            If you try to insert a node at the finishing node with insert after
            It will force you to use the insert_finish for styles purposes.
        TypeError:
            If you try to insert an element with a mismatched type of the
            Instance Type, is for avoid bugs.

    '''
    def __init__(self, genesis: BaseNode):
        self.elements = 0
        self._first_node: BaseNode = genesis

    @property
    def first_node(self) -> BaseNode:
        return self._first_node

    @first_node.setter
    def first_node(self, node: BaseNode):
        self._first_node = node

    def del_first_node(self):
        self._first_node = None

    def __len__(self):
        return self.elements

    def __repr__(self):
        return f"BaseList()\nSize:{self.elements}"

    # Metodos de la linked list
    def move_forward(self):
        node_before = None
        node = self.first_node
        while node:
            node_before = node
            node = node.next_node
        else:
            return node_before

    def _count_nodes(self):
        self.elements = 0
        if not self._first_node:
            self.elements = 0
            return
        node = self.first_node
        while node:
            self.elements += 1
            node = node.next_node

    def insert_after(self, node: BaseNode, new_node: BaseNode):
        if node.next_node:
            new_node.next_node = node.next_node
            node.next_node = new_node
        else:
            raise NODE_ASSERT_ERROR

    def insert_last(self, new_node: BaseNode):
        node = self.move_forward()
        self.elements = node.node_id + 1
        new_node.node_id = self.elements
        node.next_node = new_node

    def insert_first(self, new_node: BaseNode):

        if not self.first_node:
            self.first_node = new_node
        else:
            new_node.next = self.first_node
            self.first_node = new_node

    def remove_after(self, node: BaseNode):
        if node.next_node.next_node:
            node_to_remove = node.next_node
            node.next_node = node.next_node.next_node
            node_to_remove = None
        else:
            node_to_remove = node.next_node
            node.next_node = None
            node_to_remove = None
