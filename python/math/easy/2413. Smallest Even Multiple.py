class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 == 1:   ## 记得取余数是%，条件是==，if语句后面要加冒号
            return 2 * n
        else:
            return n
        
if __name__ == "__main__":
    sol = Solution()
    res = sol.smallestEvenMultiple(5)
    print(res)    