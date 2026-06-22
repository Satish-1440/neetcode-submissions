class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        final_dict = {}
        for i in nums:        
            if i in final_dict:
                final_dict[i] += 1
                
                return True
            final_dict[i] = 1

        return False
        