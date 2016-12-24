import enum
import enumfields


class EnumEnum(enum.Enum):
    A = 1
    B = 2


class EnumFieldsEnum(enumfields.Enum):
    A = 1
    B = 2

    class Labels:
        A = 'a label'
        B = 'b label'
