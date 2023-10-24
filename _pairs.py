from ._tbl_class import Table


class _PairsTableIterator:
    def __init__(self, table: Table, only_index:bool):
        self._dict = self._table_to_dict(table)
        self._only_index = only_index

    def __iter__(self):
        if self._only_index:
            return iter(self._dict)
        else:
            return iter(self._dict.items())

    def _table_to_dict(self, table: Table):
        dict = {}

        # Get all string index values
        for i in dir(table):
            if i[0] != "_":
                dict[i] = getattr(table, i)
        
        # Get all number index values
        for k, v in table._num_dict.items():
            dict[k] = v

        return dict


class _IpairsTableIterator(_PairsTableIterator):
    def __init__(self, table: Table, only_index:bool):
        super().__init__(table, only_index)
        self._table = table

    def __iter__(self):
        if self._only_index:
            return iter(range(1, len(self._table)+1))
        else:
            started = False
            n = 0
            list = []

            for k, v in self._dict.items():
                if k == 1:
                    started = True

                if started:
                    if k == n + 1:
                        list.append(v)
                        n = k
                    else:
                        break

            return iter(enumerate(list, 1))
    

def pairs(table: Table, only_index=False):
    """Returns a "pairs" table iterator."""
    return _PairsTableIterator(table, only_index)


def ipairs(table: Table, only_index=False):
    """Returns a "ipairs" table iterator."""
    return _IpairsTableIterator(table, only_index)
