class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        if n <= 0:
            return False
        c = 1
        while c <= n:
            if c == n:
                return True
            c = 4 * c
        return False
        """
        if n > 0 and (n & (n - 1) == 0) and n % 3 == 1:
            return True
        else:
            return False
    
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.isPowerOfFour(16)
    print(res)