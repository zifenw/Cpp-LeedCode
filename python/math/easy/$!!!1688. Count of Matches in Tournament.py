class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        matches = 0
        while n > 1:
            matches += n // 2
            if n % 2 == 0:
                n = n // 2  
            else:
                n = (n - 1) // 2 + 1
        return matches
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.numberOfMatches(7)
    print(res)

''' ***
just like 1st bit everyone else, the answer could be n - 1
every loser leave the game since a match, so we can get 1st by n - 1 matches
'''