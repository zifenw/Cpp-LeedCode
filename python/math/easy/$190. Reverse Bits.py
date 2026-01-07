class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        res << 1 左移,为新 bit 腾出空间
        n & 1 → 取最低位
        | (or) 拼接
        for _ in range(32) 循环32次
        """
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res
    ''' 不用 or 直接加
        for i in range(32):
            res = res << 1
            res += (n & 1)
            n = n >> 1
        return res
    '''
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.reverseBits(43261596)
    print(res)        