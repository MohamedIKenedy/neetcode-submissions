import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        for i in range(len(nums)):
            product_list = [element for index, element in enumerate(nums) if index!=i]
            # print(product_list)
            result.append(math.prod(product_list))
        
        return result
        