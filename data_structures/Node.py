from typing import Optional


class Node:
    def __init__(self) -> None:
        """
        Initialize a Node for a doubly-linked list.

        This class represents a Node in a doubly-linked list data structure. Each node
        contains a reference to the next node and the previous node in the list.

        Attributes:
        - self.__next (Optional[Node]): Reference to the next node in the list.
        - self.__prev (Optional[Node]): Reference to the previous node in the list.
        """
        self.__next = None
        self.__prev = None

    def get_next(self) -> Optional["Node"]:
        """
        Get the next node in the list.

        Returns:
        - Optional[Node]: The next node in the list or None if there is no next node.
        """
        return self.__next

    def get_prev(self) -> Optional["Node"]:
        """
        Get the previous node in the list.

        Returns:
        - Optional[Node]: The previous node in the list or None if there is no previous node.
        """
        return self.__prev

    def set_next(self, node: Optional["Node"]) -> None:
        """
        Set the next node in the list.

        Parameters:
        - node (Optional[Node]): The node to set as the next node in the list.
        """
        self.__next = node

    def set_prev(self, node: Optional["Node"]) -> None:
        """
        Set the previous node in the list.

        Parameters:
        - node (Optional[Node]): The node to set as the previous node in the list.
        """
        self.__prev = node
