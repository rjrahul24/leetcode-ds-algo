class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(0, len(nums)):
            if len(nums) >= 2:
                for j in range(i+1, len(nums)):
                    if (nums[i] + nums[j] == target):
                        return i,j
            else:
                return 0
                
            
                
                
                
                    
                