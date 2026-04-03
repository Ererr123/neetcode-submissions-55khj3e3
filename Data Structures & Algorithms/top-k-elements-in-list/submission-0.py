class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        
        res = []
        for _ in range(k):
            max_key = max(hashmap, key=hashmap.get)
            res.append(max_key)
            hashmap.pop(max_key)
        return res