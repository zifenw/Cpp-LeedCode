class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(num):
            for d in str(num):
                if d == '0' or num % int(d) != 0:
                    return False
            return True     ##大写Boolean
        return [x for x in range(left, right + 1) if is_self_dividing(x)]
        '''
        res = []
        for num in range(left, right + 1):
            n = num
            while n > 0:
                digit = n % 10
                if digit == 0 or num % digit !=0:
                    break       
                n = n // 10
            else:          **while-else:当while循环正常结束时会执行else**
                res.append(num)
        return res
        '''
if __name__ == "__main__":
    sol = Solution()
    res = sol.selfDividingNumbers(1, 22)
    print(res)