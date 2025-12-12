class Name:
    def __init__(self, name: str):
        self.__name: str = name

    @property
    def name (self):
        return self.__name
    @name.setter
    def name (self, value):
        if self.__name is None:
            self.__name = value   #checking wheatertje name is not empty
        else:
            raise Exception("Name is read only")
        

