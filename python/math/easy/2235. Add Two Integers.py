class Solution(object):
    def sum(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        return num1 + num2
    
# ====== 测试代码（自己加的）======
if __name__ == "__main__":
    sol = Solution()
    result = sol.sum(12, 5)
    print(result)