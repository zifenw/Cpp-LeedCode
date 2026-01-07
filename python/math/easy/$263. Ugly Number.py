class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        丑数只允许质因子 2、3、5。
        不断地 把 n 中的 2、3、5 除干净
        如果最后剩下的是 1 → 是丑数
        如果中途除不动且 n ≠ 1 → 不是丑数
        """
        if n <= 0:
            return False

        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1

if __name__ == "__main__":
    sol = Solution()
    res = sol.isUgly(49)
    print(res)