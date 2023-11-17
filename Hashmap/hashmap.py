class hashtable:
    def __init__(self):
        self.dic = {}
        self.size = 1000
        self.arr = [None for i in range(self.size)]
    def hash_func(self, key):
        index = 0
        for i in key:
            index += ord(i)
        return index

    def __setitem__(self, key, value):
        self.arr[self.hash_func(key)] = value
    def __getitem__(self,key):
        return self.arr[self.hash_func(key)]
    def __delitem__(self, key):
        self.arr[self.hash_func(key)]=None



ht = hashtable()
ht['A']=120
ht['B']=100
print(ht['B'])
del ht['B']
print(ht['B'])
print(ht['A'])
