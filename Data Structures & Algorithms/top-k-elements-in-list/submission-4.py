class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        heaplist = [(-count, num) for num, count in hashmap.items()]

        heapq.heapify(heaplist)

        for i in range(k):
            count, num = heapq.heappop(heaplist)
            res.append(num)
        
        return res
