import bisect 

class PriorityQueue():
    
    def __init__(self, order=min, f=lambda x: x):
        self.A = []
        self.f = f

    def append(self, node):
        """append in sorted order (value of f(), node)"""
        bisect.insort(self.A, (self.f(node['f']), node))

    def __len__(self):
        return len(self.A)

    def pop(self):
        return self.A.pop(0)[1]

    def __contains__(self, item):
        return any(item == node[1]["state"] for node in self.A)

    def __getitem__(self, key):
        for _, item in self.A:
            if item["state"] == key["state"]:
                return item

    def __delitem__(self, key):
        #self.A.pop(key)
        for i, item in enumerate(self.A):
            if item[1]["state"] == key["state"]:
                self.A.pop(i)
                
    def __repr__(self):
        for i in self.A:
            print (i[1], "\n")
        return ""