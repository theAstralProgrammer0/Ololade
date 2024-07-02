#!/usr/bin/python3
"""
    This is the module containing the Singly Linked List Class and Node Class
"""


class Node:
    """
        This is the Node Class definition
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
        This is the SinglyLinkedList Class definition
    """
    def __init__(self):
        """
            This is the __init__ Method definition for the singly linked list
        """
        self.head = None

    def sorted_insert(self, value):
        """
            This is the sorted_insert Method definition
        """
        newnode = Node(value)

        if not self.head:
            self.head = newnode
            return

        current = self.head
        while current.next_node:
            current = current.next_node

        current.next_node = newnode

    def __str__(self):
        """
            This is the __str__ Method definition for the singly linked list
        """
        result = []
        current = self.head

        while current:
            result.append(str(current.data))
            current = current.next_node
        result = sorted(result, key=lambda x: int(x))
        return '\n'.join(result)
