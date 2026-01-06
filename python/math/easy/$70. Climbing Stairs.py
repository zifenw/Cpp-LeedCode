class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        Fn: from Fn-1(x types) and Fn-2(y types)
        From Fn-2 but not pass Fn-1 only one type, two stair
        From Fn-1 also one type, one stair
        Fn = Fn-1 + Fn-2 (与斐波那契类似)
        """
        a, b = 1, 2
        if n == 1:
            return a
        if n == 2:
            return b
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b     
if __name__ == "__main__":
    sol = Solution()
    res = sol.climbStairs(3)
    print(res)