class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        s = 0
        if n == 0:
            return s
        if n == 1:
            return l
        count = 1
        while count < n:
            ol = l
            l = l + s
            s = ol
            count += 1
        return l
        '''斐波那契双变量解法（迭代）
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
        '''    
if __name__ == "__main__":
    sol = Solution()
    res = sol.fib(7)
    print(res)