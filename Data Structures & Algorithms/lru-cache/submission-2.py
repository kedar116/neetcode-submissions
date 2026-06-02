class LRUCache:

    def __init__(self, capacity: int):
        self.cache=[]
        self.capacity=capacity
        
    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0]==key:
                value=self.cache[i][1]
                item=self.cache.pop(i)
                self.cache.append(item)
                return value
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0]==key:
                self.cache.pop(i)
                self.cache.append([key,value])
                return 

        if len(self.cache)==self.capacity:
            del self.cache[0]

        self.cache.append([key,value])
