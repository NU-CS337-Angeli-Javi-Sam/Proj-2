from typing import List

from data_structures.DependencyParser import DependencyParser


def parse_instruction(instruction: str) -> List["str"]:
  parser = DependencyParser()

  return parser.parse(instruction)
