class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        sign = "-" if num < 0 else ""
        num = abs(num)

        # res = []
        # while num > 0:
        #     res.append(str(num % 7))
        #     num //= 7
        # return sign + "".join(reversed(res))
    
        res = ""
        while num > 0:
            res = str(num % 7) + res
            num //= 7
        return sign + res
    '''
    s = ""
    for c in ["a", "b", "c"]:
        s += c
    每次用 + 拼接字符串，都会创建一个新的字符串对象

    .join(["a", "b", "c"])一次性把所有字符写进去

    表示“用什么作为分隔符”
    "-".join(["a", "b", "c"])  # "a-b-c"
    "".join(["a", "b", "c"])  # "abc"
    '''
if __name__ == "__main__":
    sol = Solution()
    res = sol.convertToBase7()
    print(res)