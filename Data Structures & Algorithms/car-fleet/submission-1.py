class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap={}
        for i in range(len(position)):
            hashmap[position[i]]=speed[i]
        hashmap_dec=sorted(hashmap.keys(), reverse=True)

        stack=[]
        for pos in hashmap_dec:
            stack.append((target-pos)/hashmap[pos])
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)