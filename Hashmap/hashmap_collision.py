class hashtable:
    def __init__(self):
        self.dic = {}
        self.size = 10
        self.arr = [[] for i in range(self.size)]
    def hash_func(self, key):
        index = 0
        for i in key:
            index += ord(i)
        return index % self.size

    def __setitem__(self, key, value):
        found=False
        for index,element in enumerate(self.arr[self.hash_func(key)]):
            if len(element)==2 and element[0]==key:
                self.arr[self.hash_func(key)][index]=(key,value)
                found=True
                break
        if found==False:
            self.arr[self.hash_func(key)].append((key,value))

    def __getitem__(self,key):
        for index,element in enumerate(self.arr[self.hash_func(key)]):
            if element[0]==key:
                return element[1]
    def __delitem__(self, key):

        for index,element in enumerate(self.arr[self.hash_func(key)]):
            if element[0]==key:
                del self.arr[self.hash_func(key)][index]



ht = hashtable()
print(ht.hash_func('march 6'))
ht['march 6']=120
print(ht.hash_func('march 17'))
ht['march 17']=199
print(ht['march 17'])
ht['march 1']=2
print(ht['march 2'])
print(ht.arr)
del ht['march 17']
print(ht.arr)