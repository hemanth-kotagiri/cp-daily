class HashMap:
    def __init__(self):
        self.hashmap = {}

    def update(self, key, val):
        self.hashmap[key] = val

    def get(self, key):
        if key not in self.hashmap.keys():
            return None
        return self.hashmap[key]

    def max_key(self, val):
        max_key = float('-inf')
        for key, value in self.hashmap.items():
            if value == val and key > max_key:
                max_key = key
        return max_key if max_key != float('-inf') else None

#obj = HashMap()
#obj.update(1, 20)
#obj.update(2, 20)
#obj.update(3, 20)
#obj.update(4, 20)
#print(obj.max_key(40))
#print(obj.get(50))

class Node:
    def __init__(self, key, value):
        try:
            self.key = key
            self.val = value
        except:
            print("INVALID")
            exit(-1)

class KeyValue:
    def __init__(self):
        self.arr = []

    def update(self, key, val):
        for i in self.arr:
            if i.key == key:
                i.val = val
                return
        self.arr.append(Node(key, val))

    def get(self, key):
        for i in self.arr:
            if i.key == key:
                return i.val
        return None
    
    def max_key(self, val):
        found = False
        m = float('-inf')
        if len(self.arr) == 0: return None
        for node in self.arr:
            if node.val == val and node.key > m:
                m = node.key
                found = True
        return m if found else None


kv = KeyValue()
kv.update(1, 1)
kv.update(2, 1)
kv.update(3, 20)
print(kv.get(3))
print(kv.max_key(1))
print(kv.max_key(40))




kk = KeyValue()

kv.update('asd', 2)









