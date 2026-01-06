class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        product = 1 ## be careful
        for d in str(n):
            digit = int(d)
            sum += digit
            product *= digit
        return product - sum 
if __name__ == "__main__":
    sol = Solution()
    res = sol.subtractProductAndSum(4421)
    print(res)