from ._pairs import ipairs, pairs
from ._tbl_class import Table
from typing import Any
import os


_TABLE_LIBRARY_AS_TABLE_OBJECT = os.path.isfile(os.getcwd() + "/table_library")


def _table_can_shift(table: Table, pos: int) -> bool:
    for k in ipairs(table, True):
        if k == pos:
            return True

    return False


def _table_shift(table: Table, pos: int, shift:int):
    started = False
    for k, v in ipairs(table):
        if k == pos:
            table[k] = None
            started = True

        if started:
            table[k + shift] = v

    if not started:
        return False
    
    return True


def _table_insert_last(table: Table, value: Any):
    table[len(table) + 1] = value


def _table_insert_pos(table: Table, pos: int, value: Any):
    if not isinstance(pos, int):
        raise TypeError("position argument must be of type 'int'")

    if _table_can_shift(pos):
        table[pos] = value
        _table_shift(table, pos, 1)
    else:
        raise TypeError("bad argument 'position' to 'insert' (position out of bounds)")


def _table_remove_last(table: Table) -> Any:
    val = table[len(table)]
    table[len(table)] = None
    return val


def _table_remove_pos(table: Table, pos: int) -> Any:
    if not isinstance(pos, int):
        raise TypeError("position argument must be of type 'int'")
    
    val = table[pos]

    if _table_can_shift(pos):
        _table_shift(table, pos, -1)
    else:
        raise TypeError("bad argument 'position' to 'insert' (position out of bounds)")
    
    return val


# 'table' library
class table:
    def __new__(cls):
        raise TypeError("cannot create 'table' instances")

    def insert(t: Table, *args: Any) -> None:
        """
        table.insert(table:Table, element:Any) - Append an element to the table
            or
        table.insert(table:Table, position:int, element:Any) - Insert an element at index 'position' and shift the following indexes up by one step
        """

        match len(args):
            case 1:
                _table_insert_last(t, args[0])
            case 2:
                _table_insert_pos(t, args[0], args[1])
            case _:
                raise TypeError("wrong number of arguments to 'insert'")

    def remove(t: Table, *args) -> Any:
        """
        table.remove(table:Table, position:int) - something
            or
        table.remove(table:Table) - something
        """
        match len(args):
            case 0:
                return _table_remove_last(t)
            case 1:
                return _table_remove_pos(t, args[0])
            case _:
                raise TypeError("wrong number of arguments to 'remove'")
    
    # def eremove( t:Table, element:Any, amount ) -> Any:
    #     for k, v in pairs(t):
    #         if v==element:
    #             t[k] = None

    # def count( t:Table ) -> int:
    #     print(t)


if _TABLE_LIBRARY_AS_TABLE_OBJECT:
    table_class = table
    table = Table()  # 'table' library as 'Table' object

    for attr in dir(table_class):
        if attr[0] != "_":
            table[attr] = getattr(table_class, attr)
