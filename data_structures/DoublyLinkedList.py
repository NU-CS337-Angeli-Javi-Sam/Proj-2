from typing import Any, Optional
from data_structures.Node import Node

class DoublyLinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__length = 0

    def __str__(self) -> str:
        curr_node = self.get_head()
        output = ""
        while curr_node:
            output += f"{curr_node.get_data()} <-> "
            curr_node = curr_node.get_next()

        output += "None"
        return output

    def __len__(self) -> int:
        return self.get_length()

    def get_head(self) -> Optional["Node"]:
        return self.__head

    def get_tail(self) -> Optional["Node"]:
        return self.__tail

    def get_length(self) -> int:
        return self.__length

    def __set_head(self, node: Optional["Node"]) -> None:
        self.__head = node

    def __set_tail(self, node: Optional["Node"]) -> None:
        self.__tail = node

    def __set_length(self, length: int) -> None:
        self.__length = length

    def __increment_length(self) -> None:
        self.__set_length(self.__length + 1)

    def push(self, data: Optional["Node"]) -> None:
        new_node = Node(data)

        if self.get_head() is None:
            self.__set_head(new_node)
            self.__set_tail(new_node)
            self.__increment_length()
            return

        head = self.get_head()
        head.set_prev(new_node)
        new_node.set_next(head)
        self.__set_head(new_node)
        self.__increment_length()

    def append(self, data: Optional["Node"]) -> None:
        new_node = Node(data)

        if self.get_head() is None:
            self.__set_head(new_node)
            self.__set_tail(new_node)
            self.__increment_length()
            return

        tail = self.get_tail()
        tail.set_next(new_node)
        new_node.set_prev(tail)
        self.__set_tail(new_node)
        self.__increment_length()

    def insertAt(self, data: Optional["Node"], index: int) -> None:

        if index < 0 or index > self.get_length():
            raise IndexError("Index is out of range")

        if index == 0:
            self.push(data)
            return
        elif index == self.get_length():
            self.append(data)
            return

        new_node = Node(data)

        curr_node = self.get_head()
        curr_node_index = 0
        while curr_node_index != index:
            curr_node = curr_node.get_next()
            curr_node_index += 1

        curr_node.get_prev().set_next(new_node)
        new_node.set_prev(curr_node.get_prev())
        curr_node.set_prev(new_node)
        new_node.set_next(curr_node)
        self.__increment_length()

    def get_node_at(self, index: int) -> None:
        if index < 0 or index > self.get_length():
            raise IndexError("Index is out of range")

        curr_node = self.get_head()
        curr_node_index = 0
        while curr_node_index != index:
            curr_node = curr_node.get_next()
            curr_node_index += 1

        return curr_node

    def get_data_at(self, index: int) -> Any:
        node = self.get_node_at(index)
        return node.get_data()

    def clear(self) -> None:
        self.__set_head(None)
        self.__set_tail(None)
        self.__set_length(0)

    def reverse(self) -> None:
        curr_node = self.get_head()
        self.__set_head(self.get_tail())
        self.__set_tail(curr_node)
        while curr_node != None:
            temp = curr_node.get_next()
            curr_node.set_next(curr_node.get_prev())
            curr_node.set_prev(temp)
            curr_node = curr_node.get_prev()
