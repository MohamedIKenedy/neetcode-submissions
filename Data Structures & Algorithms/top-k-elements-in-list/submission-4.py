class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        results = []
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        
        sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)) 
        print(sorted_dict)
        temp = []

        for i, (key,v) in enumerate(sorted_dict.items()):
            print(i)
            if i < k:
                results.append(key)
        
        return results

            
        