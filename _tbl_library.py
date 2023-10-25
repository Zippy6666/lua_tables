from ._pairs import ipairs
from ._tbl_class import Table
from typing import Any
import os


_TABLE_LIBRARY_AS_TABLE_OBJECT = os.path.isfile(os.getcwd() + "/table_library")


def _table_insert_last(table: Table, value: Any):
    table[len(table) + 1] = value


def _table_insert_pos(table: Table, pos: int, value: Any):
    if not isinstance(pos, int):
        raise TypeError("position argument must be of type 'int'")

    started = False
    for k, v in ipairs(table):
        if k == pos:
            table[k] = value
            started = True

        if started:
            table[k + 1] = v

    if not started:
        raise TypeError("bad argument 'position' to 'insert' (position out of bounds)")


# 'table' library
class table:
    def __new__(cls):
        raise TypeError("cannot create 'table' instances")

    def insert(table: Table, *args: Any) -> None:
        """
        Syntax:
                table.insert(table:Table, element:Any)
            or
                table.insert(table:Table, position:int, element:Any)

        From lua.org:
            \"The table.insert function inserts an element in a given position of an array, moving up other elements to open space.\"
            \"As a special (and frequent) case, if we call insert without a position, it inserts the element in the last position of the array (and, therefore, moves no elements).\"
        """

        match len(args):
            case 1:
                _table_insert_last(table, args[0])
            case 2:
                _table_insert_pos(table, args[0], args[1])
            case _:
                raise TypeError("wrong number of arguments to 'insert'")

    def remove(table: Table):
        pass

    def RemoveByValue(table: Table):
        pass

    def Count(table: Table):
        pass

    def IsEmpty(table: Table):
        pass

    def Empty(table: Table):
        pass

    def Random(table: Table):
        pass


def PrintTable(table: Table) -> None:
    pass


if _TABLE_LIBRARY_AS_TABLE_OBJECT:
    table_class = table
    table = Table()  # 'table' library as 'Table' object

    for attr in dir(table_class):
        if attr[0] != "_":
            table[attr] = getattr(table_class, attr)
