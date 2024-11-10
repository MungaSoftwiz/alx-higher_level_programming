class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): A reference to the next node in the list.

    Methods:
        data: Property to retrieve the data stored in the node.
        data: Setter to update data stored in the node.
        next_node: Property to retrieve the next node.
        next_node: Setter to update the next node.
    """
    def __init__(self, data, next_node=None):
        """
        Initialize a new node with the given data and optional next node.

        Args:
            data (int): The data to store in the node.
            next_node (Node or None, optional): The next node in the list.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieve the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data for the node, ensuring it is an integer.

        Args:
            value (int): The data to store in the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node for the current node.

        Args:
            value (Node or None): The next node to link to.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node or None): The head (first node) of the list.

    Methods:
        __str__: Returns a string representation of the list.
        sorted_insert: Inserts a new node with the given value into
        the list while maintaining order.
    """
    def __init__(self):
        """
        Initialize an empty singly linked list with no head node.
        """
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the list,
        with each node's data printed on a new line.

        Returns:
            str: The string representation of the list.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Insert a new node with the specified value
        into the list, while maintaining sorted order.

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
