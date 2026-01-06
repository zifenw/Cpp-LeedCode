class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        ## str(num) 把整数转成字符串
        ## sorted() 函数对可迭代的对象进行排序，返回一个新的列表
        digits = sorted([int(d) for d in str(num)])  ## 列表生成式
        ## disits = sorted(map(int, str(num)))  ## 另一种写法，map() 函数将 str(num) 中的每个字符转换为整数 
        return (digits[0] * 10 + digits[2]) + (digits[1] * 10 + digits[3])
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.minimumSum(2932)
    print(result)

    