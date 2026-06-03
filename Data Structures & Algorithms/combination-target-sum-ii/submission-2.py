class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def generate_subsets(i, curr, total):
            if total==target:
                res.append(curr.copy())
                return
            if i>=len(candidates) or total>target:
                return

            #include
            curr.append(candidates[i])
            generate_subsets(i+1, curr, total+candidates[i])

            #exclude
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1
            curr.pop()
            generate_subsets(i+1, curr, total)

        generate_subsets(0, [], 0)

        return res