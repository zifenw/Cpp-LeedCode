class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for d in str(num):
            digit = int(d)
            if digit != 0 and num % digit == 0:
                count += 1
        return count
if __name__ == "__main__":
    sol = Solution()
    result = sol.countDigits(121)
    print(result)

    """ Example Output: 2 
    
    
    """