class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        power = 1
        while power <= n:
            if n == power:
                return True
            power = power * 2
        return False
if __name__ == "__main__":
    sol = Solution()
    res = sol.isPowerOfTwo(128)
    print(res)