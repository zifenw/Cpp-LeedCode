class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num % 10 != 0 or num == 0:
            return True
        else:
            return False
if __name__ == "__main__":
    sol = Solution()
    res = sol.isSameAfterReversals(526)
    print(res)