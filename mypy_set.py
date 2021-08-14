from typing import Set

X: Set[int] = {1}
print("a" in X)
X.__contains__("a")
