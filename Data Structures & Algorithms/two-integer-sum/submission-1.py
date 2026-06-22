class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in d:
                print([d[j],i])
                return[d[j],i]
            d[nums[i]] = i
      