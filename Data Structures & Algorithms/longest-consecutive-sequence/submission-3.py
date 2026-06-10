class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_count = 0

        if nums == []:
            return 0
        
        for i in range(len(nums)):
            if nums[i] - 1 not in numSet:
                count = 1
                j = 1
                while nums[i] + j in numSet:
                    count +=1
                    j +=1
                if count >= max_count:
                    max_count = count
                    
        return max_count