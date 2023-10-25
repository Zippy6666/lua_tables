from typing import Any


class Table:
    def __init__(self, *args: Any, dict: dict[(str,int,float), Any] = {}, **kwargs: dict[str, Any]):
        """
        Returns a lua inspired table object.

        The table type is a associative array. They are the only data structuring mechanism in Lua.
        Tables can be used to represent anything from ordinary arrays, to dictionaries or other data structures, in one single, efficient way.
            
        Features
            - Two ways to index: Table.x, Table["x"]
            - Setting a value to None will remove it from the table
            - Does not raise IndexError, KeyError, or AttributeError, it instead returns None
            - len() works like the "#" operator in lua
        
        Note: Only supports strings and numbers as indexes!
        """

        self._num_dict = {}

        # Arguments
        for i, v in enumerate(args, 1):
            self._num_dict[i] = v

        # Keyword arguments
        for k, v in kwargs.items():
            setattr(self, k, v)

        # Dictionary argument
        for k, v in dict.items():
            self[k] = v

    def _index_type_check(func):
        """Raise error if index is not int, float or str"""

        def wrapper(self, index, *args):
            if not isinstance(index, (int, float, str)):
                raise TypeError("table index must be a string or a number")
            return func(self, index, *args)

        return wrapper

    @_index_type_check
    def __setitem__(self, index, value):
        # String index
        if isinstance(index, str):
            if value is None:
                delattr(self, index)
            else:
                setattr(self, index, value)

        # Number index
        elif isinstance(index, (int, float)):
            if value is None:
                del self._num_dict[index]
            else:
                self._num_dict[index] = value

    @_index_type_check
    def __getitem__(self, index):
        # String index
        if isinstance(index, str):
            if hasattr(self, index):
                return getattr(self, index)
            else:
                return None

        # Number index
        elif isinstance(index, (int, float)):
            if index in self._num_dict:
                return self._num_dict[index]
            else:
                return None

    def __setattr__(self, attr, value):
        if value is None:
            delattr(self, attr)
        else:
            super().__setattr__(attr, value)

    def __getattr__(self, attr):
        try:
            return super().__getattr__(attr)
        except AttributeError:
            return None

    def __len__(self):
        n = 0
        started_counting = False

        for k in self._num_dict:
            if k == 1:
                started_counting = True

            if started_counting:
                if k == n + 1:
                    n = k
                else:
                    break

        return n

    def __repr__(self):
        return f"table: {hex(id(self))}"
    
    def __iter__(self):
        raise TypeError("'Table' object is not iterable")


def main():
    pass


if __name__ == "__main__":
    main()
