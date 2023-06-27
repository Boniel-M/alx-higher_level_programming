#!/usr/bin/python3
"""
This module defines a class Node that represents a square shape.

"""


class Node:
    """
    A class representing a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node (private).
        __next_node (Node): The next node in the linked list (private).
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): The next node in the linked list (default None).

        Raises:
            TypeError: If data is not an integer or
            next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head: The head (first node) of the linked list.
    """

    def __init__(self):
        """
        Initializes a SinglyLinkedList instance.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The value of the new Node to be inserted.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                    value >= current.next_node.data):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node

        return '\n'.join(nodes)
