class Makeup:
    
    all = []

    def __init__(self, brand, type):
        self.brand = brand
        self.type = type

        Makeup.all.append(self)

        self._owners = []
        self._purchases = []

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if type(brand) == str:
            self._brand = brand
        else:
            raise Exception("brand must be a string")
        
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, new_type):
        if type(new_type) == str:
            self._type = new_type
        else:
            raise Exception("type must be a string")
        
    @classmethod
    def get_unique_types(cls):
        # unique_types = []
        # for makeup in cls.all:
        #     if makeup.type not in unique_types:
        #         unique_types.append(makeup.type)
        # return unique_types
        return list(set([makeup.type for makeup in cls.all]))
        
    def __repr__ (self):
        return f"{self.brand} {self.type}"