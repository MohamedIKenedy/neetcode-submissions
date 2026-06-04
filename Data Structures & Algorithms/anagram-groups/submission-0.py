class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signature = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in signature:
                signature[key] = []
            signature[key].append(word)
        
        results = []
        for k, v in signature.items():
            results.append(v)
        
        return results


        