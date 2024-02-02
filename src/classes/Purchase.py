class Purchase:
    all = []

    def __init__(self, makeup_item, person, date):
        self.makeup_item = makeup_item
        self.person = person
        self.date = date

        #add links for People objects
        self.person._makeup_item.append(self.makeup_item)
        self.person._purchases.append(self)

        #add links for Makeup objects
        self.makeup_item._owners.append(self.person)
        self.makeup_item._purchases.append(self)

        Purchase.all.append(self)

    @property
    def makeup_item(self):
        return self._makeup_item
    
    @makeup_item.setter
    def makeup_item(self, new_makeup_item):
        from Makeup import Makeup
        if isinstance(new_makeup_item, Makeup):
            self._makeup_item = new_makeup_item
        else:
            raise Exception("makeup_item must be a Makeup object")
    
    @property
    def person(self):
        return self._person
    
    @person.setter
    def person(self, person):
        from People import People
        if isinstance(person, People):
            self._person = person
        else:
            raise Exception("person must be a People object")
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if type(date) == str:
            self._date = date
        else:
            raise Exception("date must be a string")
        
    @classmethod
    def get_most_popular_brand(cls):
        brand_freq = {}
        for purchase in cls.all:
            brand = purchase.makeup_item.brand
            if brand not in brand_freq:
                brand_freq[brand] = 1
            else:
                brand_freq[brand] += 1
        return max(brand_freq, key = brand_freq.get)