class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ''''
        range
        从 start 开始（包含 start）
        到 end 结束，但 不包含 end
        '''
        count = 0
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count ## different when tab this line
        '''
        Counting factors of a single number n
        for (count < small // count):
        for i in range(1, sqrt(n)+1):
        '''
        
if __name__ == "__main__":
    sol = Solution()
    res = sol.commonFactors(12, 6)
    print(res)