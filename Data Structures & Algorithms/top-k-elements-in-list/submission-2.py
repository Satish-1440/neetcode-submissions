class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        
        for num in hash_map:
            frequency = hash_map[num]
            bucket[frequency].append(num)
        print(bucket)
        result = []
        for i in range(len(bucket)-1, -1,-1):
            for m in bucket[i]:
                result.append(m)
                if len(result) == k:
                    return result
        return result 

        