from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        self.__data = data
        self.__next = None
        self.__prev = None

    def get_data(self) -> Any:
        return self.__data

    def get_next(self) -> Optional["Node"]:
        return self.__next

    def get_prev(self)-> Optional["Node"]:
        return self.__prev

    def set_data(self, data: Optional["Node"]) -> None:
        self.__data = data

    def set_next(self, node: Optional["Node"]) -> None:
        self.__next = node

    def set_prev(self, node: Optional["Node"]) -> None:
        self.__prev = node
