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

    def _key_type_check(func):
        """Raise error if key is not int, float or str"""

        def wrapper(self, key, *args):
            if not isinstance(key, (int, float, str)):
                raise TypeError("Table index must be a string or a number!")
            return func(self, key, *args)

        return wrapper

    @_key_type_check
    def __setitem__(self, key, value):
        if isinstance(key, str):
            if value is None:
                delattr(self, key)
            else:
                setattr(self, key, value)

        elif isinstance(key, (int, float)):
            if value is None:
                del self._num_dict[key]
            else:
                self._num_dict[key] = value

    @_key_type_check
    def __getitem__(self, key):
        if isinstance(key, str):
            if hasattr(self, key):
                return getattr(self, key)
            else:
                return None

        elif isinstance(key, (int, float)):
            if key in self._num_dict:
                return self._num_dict[key]
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
    for i in Table():
        print(i)


if __name__ == "__main__":
    main()
