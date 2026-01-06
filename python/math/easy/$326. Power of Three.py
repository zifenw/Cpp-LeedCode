class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        if n <= 0:
            return False
        c = 1
        while c <= n:
            if c == n:
                return True
            c = c * 3
        return False
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1        
if __name__ == "__main__":
    sol = Solution()
    res = sol.isPowerOfThree(27)
    print(res)