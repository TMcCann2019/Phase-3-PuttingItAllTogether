class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        self._makeup_item = []
        self._purchases = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name') and type(name) == str:
            self._name = name
        else:
            raise Exception("name must be a string and cannot be mutated")
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if type(age) == int and age > 12:
            self._age = age
        else:
            raise Exception("age must be an integer and greater than 12")
        
    def __repr__(self):
        return f"{self.name}"