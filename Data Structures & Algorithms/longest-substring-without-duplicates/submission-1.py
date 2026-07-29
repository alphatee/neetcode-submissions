class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0 # handles empty string 
        l, r = 0, 0 # start both pointers at index 0, to catch the first character 
        length = 0
        hash = {} 

        while r < len(s): 
            if s[r] in hash and hash[s[r]] >= l:
                l = hash[s[r]] + 1 # update l to skip a repeat

            hash[s[r]] = r # store the index of the character 

            length = max(length, r - l + 1) # length of the current window size, dynamically changes 
            r += 1

        return length 