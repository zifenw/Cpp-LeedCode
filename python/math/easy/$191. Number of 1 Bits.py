class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int

        while n: 在n不为0之前一直运行。等于while n > 0:
        """
        c = 0
        while n:
            c += n & 1
            n >>= 1
        return c

if __name__ == "__main__":
    sol = Solution()
    res = sol.hammingWeight(11)
    print(res)        