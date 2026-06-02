class TimeMap:

    def __init__(self):
        self.hashmap=defaultdict(list)
        result=[]
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value,timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        ans=""
        left=0
        right=len(self.hashmap[key])-1
        while left<=right:
            mid=(left+right)//2
            val=self.hashmap[key][mid][1]
            if val <= timestamp:
                ans=self.hashmap[key][mid][0]
                left=mid+1
            else:
                right=mid-1
        return ans
