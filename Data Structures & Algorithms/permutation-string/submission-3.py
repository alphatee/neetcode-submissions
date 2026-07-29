from collections import Counter 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False 

        s1_sum = sum(ord(c) for c in s1)
        s1_counts = Counter(s1) # Required to verify permutations

        # Calculate the sum of the very first window
        current_window_sum = sum(ord(s2[i]) for i in range(n1))

        for l in range(n2 - n1 + 1):
            r = l + n1

            # 1. Check if the sum matches 
            if current_window_sum == s1_sum:
                # 2. Verify it's a real permutation (prevents false positives)
                if Counter(s2[l:r]) == s1_counts:
                    return True

            # 3. Slide the window: subtract leftmost, add next rightmost
            if r < n2:
                current_window_sum = current_window_sum - ord(s2[l]) + ord(s2[r])

        return False