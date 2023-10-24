class Tbl():
    def __init__( self, **kwargs ):
        """ Returns a lua table object """
        self._contents = {}

        for k, v in kwargs.items():
            self._setitem( k, v )

    def __getitem__( self, index ) -> any:
        if not index in self._contents:
            return None
        
        return self._contents[index]

    def __setitem__( self, index, value ):
        self._setitem( index, value, True )

    def _setitem( self, index, value, setAttr=False ):
        if value is None:
            if index in self._contents:
                del self._contents[ index ]
            return

        self._contents[index] = value

        if setAttr is True:
            setattr(self, index, value, setItem=False)

    def __repr__( self ):
        string = "{"
        kV = self._contents.items()

        for i, (k, v) in enumerate( kV ):
            string += f"{k} = {v}"

            if i < len(kV)-1:
                string += ", "
        
        string += "}"
        return string

    def __getattr__( self, attr ):
        if attr in self._contents:
            return self._contents[attr]

    def __setattr__( self, attr, value, setItem=True ):
        if setItem is True and attr != "_contents":
            self._setitem( attr, value )

        if value is None:
            delattr(self, attr)
        else:
            super().__setattr__( attr, value )

    def __iter__( self ):
        return iter( self._contents.items() )

    def __len__( self ):
        return len( self._contents )