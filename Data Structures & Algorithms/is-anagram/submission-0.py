class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        char_freq_s = {}
        char_freq_t = {}

        for c1, c2  in zip(s,t):
            char_freq_s[c1] = s.count(c1)
            char_freq_t[c2] = t.count(c2)
        
        if char_freq_s == char_freq_t :
            return True
        else:
            return False


        
        
        

            
