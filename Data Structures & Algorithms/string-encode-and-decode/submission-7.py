import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes, res = [], []

        if not strs:
            return "None"
        
        for s in strs:
            sizes.append(len(s))

        for size in sizes:
            res.append(str(size))
            res.append(',')
        res.append('#')
        res.extend(strs)

        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        result = []
        if s == "None":
            return []
        
        parts = s.split('#', 1)
        sizes_part = parts[0]
        string = parts[1]
        
        sizes = [sz for sz in sizes_part.split(',') if sz]

        for size in sizes:
            result.append(string[:int(size)])
            string = string[int(size):]
        return result