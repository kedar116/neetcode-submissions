class TimeMap:

    def __init__(self):
        self.hashmap=defaultdict(list)
        result=[]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value,timestamp])
        return None

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        ans=""
        for val, ts in self.hashmap[key]:
            if ts<=timestamp:
                ans=val
            else:
                break
        return ans