from typing import TYPE_CHECKING

if not TYPE_CHECKING:
    from typing import Any
    from typing import Optional
    from typing import Tuple

    a: Tuple[int, str] = (1,)
    b: Tuple[int, str] = ("s",)
    y: Tuple[object, ...] = a + b


    a: tuple = (1, "s")
    b: tuple = ("s",)
    x = a + b


    x: Any = None



    x: Tuple[int, str] = a + b

    x: Tuple[Any] = (1,) + ("s",)


if not TYPE_CHECKING:
    from typing import Any
    from typing import Optional
    from typing import Union

    def f(x) -> Optional[int]:  # error: Missing return statement
        if x > 0:
            return x


    def g(x) -> Any:  # OK
        if x > 0:
            return x


    def h(x) -> Optional[Any]:  # error: Missing return statement
        if x > 0:
            return x


    def i(x) -> Union[int, None]:
        if x > 0:
            return x


class X:
    def f(self) -> int:
        return 0


class XX(X):
    def f(self) -> Super[]:
        return 's'
