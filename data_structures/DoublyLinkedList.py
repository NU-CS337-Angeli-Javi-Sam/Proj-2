from typing import Optional
from data_structures.Instruction import Instruction


class DoublyLinkedList:
    def __init__(self) -> None:
        """
        Initialize a Doubly Linked List.

        This class represents a doubly linked list data structure. It provides methods to
        manipulate the list, such as inserting, appending, getting nodes at specific
        indices, reversing the list, and more.

        Attributes:
        - self.__head (Optional[Instruction]): Reference to the head node (start) of the list.
        - self.__tail (Optional[Instruction]): Reference to the tail node (end) of the list.
        - self.__length (int): The number of nodes in the list.
        """

        self.__head = None
        self.__tail = None
        self.__length = 0

    def __str__(self) -> str:
        """
        Convert the list to a string representation.

        Returns:
        - str: A string representation of the doubly linked list.
        """
        curr_node: Instruction = self.get_head()
        output: str = ""
        count = 0
        while curr_node:
            output += f"{count + 1}) {curr_node}\n\n"
            output += f""
            curr_node: Instruction = curr_node.get_next()
            count += 1
        return output

    def __len__(self) -> int:
        """
        Get the length of the list.

        Returns:
        - int: The number of nodes in the list.
        """
        return self.get_length()

    def get_head(self) -> Optional["Instruction"]:
        """
        Get the head (start) node of the list.

        Returns:
        - Optional[Instruction]: The head node or None if the list is empty.
        """
        return self.__head

    def get_tail(self) -> Optional["Instruction"]:
        """
        Get the tail (end) node of the list.

        Returns:
        - Optional[Instruction]: The tail node or None if the list is empty.
        """
        return self.__tail

    def get_length(self) -> int:
        """
        Get the length (number of nodes) of the list.

        Returns:
        - int: The number of nodes in the list.
        """
        return self.__length

    def __set_head(self, node: Optional["Instruction"]) -> None:
        """
        Set the head (start) node of the list.

        Parameters:
        - node (Optional[Instruction]): The node to set as the head of the list.
        """
        self.__head = node

    def __set_tail(self, node: Optional["Instruction"]) -> None:
        """
        Set the tail (end) node of the list.

        Parameters:
        - node (Optional[Instruction]): The node to set as the tail of the list.
        """
        self.__tail = node

    def __set_length(self, length: int) -> None:
        """
        Set the length of the list.

        Parameters:
        - length (int): The number of nodes in the list.
        """
        self.__length = length

    def __increment_length(self) -> None:
        """
        Increment the length of the list by 1.
        """
        self.__set_length(self.__length + 1)

    def push(self, new_node: Instruction) -> None:
        """
        Push a new node with data to the front of the list.

        Parameters:
        - data (Optional["Instruction"]): The data to be added to a new node.
        """

        if self.get_head() is None:
            self.__set_head(new_node)
            self.__set_tail(new_node)
            self.__increment_length()
            return

        head: Instruction = self.get_head()
        head.set_prev(new_node)
        new_node.set_next(head)
        self.__set_head(new_node)
        self.__increment_length()

    def append(self, new_node: Instruction) -> None:
        """
        Append a new node with data to the end of the list.

        Parameters:
        - data (Optional["Instruction"]): The data to be added to a new node.
        """

        if self.get_head() is None:
            self.__set_head(new_node)
            self.__set_tail(new_node)
            self.__increment_length()
            return

        tail: Instruction = self.get_tail()
        tail.set_next(new_node)
        new_node.set_prev(tail)
        self.__set_tail(new_node)
        self.__increment_length()

    def insertAt(self, new_node: Instruction, index: int) -> None:
        """
        Insert a new node with data at a specific index in the list.

        Parameters:
        - data (Optional["Instruction"]): The data to be added to a new node.
        - index (int): The index at which to insert the new node.

        Raises:
        - IndexError: If the index is out of range.
        """
        if index == 0:
            self.push(new_node)
            return
        elif index == self.get_length():
            self.append(new_node)
            return

        curr_node: Instruction = self.get_node_at(index)

        curr_node.get_prev().set_next(new_node)
        new_node.set_prev(curr_node.get_prev())
        curr_node.set_prev(new_node)
        new_node.set_next(curr_node)
        self.__increment_length()

    def get_node_at(self, index: int) -> Optional["Instruction"]:
        """
        Get the node at a specific index in the list.

        Parameters:
        - index (int): The index of the node to retrieve.

        Returns:
        - Optional["Instruction"]: The node at the specified index or None if the index is out of range.

        Raises:
        - IndexError: If the index is out of range.
        """
        if index < 0 or index > self.get_length():
            raise IndexError("Index is out of range")

        curr_node: Instruction = self.get_head()
        curr_node_index: int = 0
        while curr_node_index != index:
            curr_node: Instruction = curr_node.get_next()
            curr_node_index += 1

        return curr_node

    def clear(self) -> None:
        """
        Clear the list by resetting head, tail, and length.
        """
        self.__set_head(None)
        self.__set_tail(None)
        self.__set_length(0)

    def reverse(self) -> None:
        """
        Reverse the order of nodes in the list.
        """
        curr_node: Instruction = self.get_head()
        self.__set_head(self.get_tail())
        self.__set_tail(curr_node)
        while curr_node != None:
            temp: Instruction = curr_node.get_next()
            curr_node.set_next(curr_node.get_prev())
            curr_node.set_prev(temp)
            curr_node: Instruction = curr_node.get_prev()
