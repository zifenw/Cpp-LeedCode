class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        
        if n <= 0:
            return False
        power = 1
        while power <= n:
            if n == power:
                return True
            power = power * 2
        return False
        """
        
        if n > 0 and (n & (n - 1)) == 0:
            return True
        else:
            return False
        ''' 2 的幂在二进制中只有一个 1
n      = 1000
n - 1  = 0111
----------------
&      = 0000
        '''
        
if __name__ == "__main__":
    sol = Solution()
    res = sol.isPowerOfTwo(128)
    print(res)