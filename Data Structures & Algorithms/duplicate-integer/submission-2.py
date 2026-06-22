class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        final_dict = {}
        for i in nums:
            if i not in final_dict:
                final_dict[i] = 0
            if final_dict[i] > 0:
                return True
            else:
                final_dict[i] += 1
        return False
