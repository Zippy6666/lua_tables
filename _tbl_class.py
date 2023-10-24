from typing import Any


class Table:
    def __init__(self, *args:Any, dict:dict={}, **kwargs: dict[str, Any]):
        """Returns a lua table object. Currently has:
            - Key, value pairs [(string, int, float), Any]
            - Setting values with item assignment
            - Setting values by setting attributes
            - Removing values by setting them to None
            - Does not raise IndexError, KeyError, or AttributeError, it instead returns None
            - Lenght
        """

        self._num_dict = {}

        # Arguments
        for i, v in enumerate(args, 1):
            self._num_dict[i] = v

        # Keyword arguments
        for k, v in kwargs.items():
            setattr(self, k , v)

        # Dictionary argument
        for k, v in dict.items():
            self[k] = v


    def _key_type_check(func):
        """ Raise error if key is not int, float or str"""

        def wrapper( self, key, *args ):
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
        for k, v in self._num_dict.items():
            print(k, v)
        return 0
    
    def __repr__(self):
        return f"table: {hex(id(self))}"

def main():
    t = Table("dog", 1, 2, 3, "fart")
    print(f"#{len(t)}")


if __name__ == "__main__":
    main()
