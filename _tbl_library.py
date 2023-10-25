from ._pairs import ipairs
from ._tbl_class import Table
from typing import Any


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


def _insert(table: Table, *args: Any) -> None:
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


def _remove(table: Table):
    pass


def _RemoveByValue(table: Table):
    pass


def _Count(table: Table):
    pass


def _IsEmpty(table: Table):
    pass


def _Empty(table: Table):
    pass


def _Random(table: Table):
    pass


table = Table()
table.insert = _insert
table.remove = _remove
table.RemoveByValue = _RemoveByValue
table.Count = _Count
table.IsEmpty = _IsEmpty
table.Empty = _Empty
table.Random = _Random


def PrintTable(table: Table) -> None:
    pass
