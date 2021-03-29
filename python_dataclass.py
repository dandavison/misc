from dataclasses import dataclass
from typing import Optional

@dataclass
class X:
    a: int
    c: int
    b: int = None

    def __repr__(self):
        return f"X(a={self.a}, b={self.b}, c={self.c})"

if False:
    print(X(1, 2))  # TypeError: non-default argument 'c' follows default argument


@dataclass
class Node:
    line_num: Optional[bool] = None


@dataclass
class BinOp(Node):
    op: str
    left: int
    right: int



print(BinOp("+", 1, 2))
