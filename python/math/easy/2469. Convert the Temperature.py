class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        ## round(kelvin, 5), round(fahrenheit, 5)
        return [kelvin, fahrenheit]
    
    """
        result =[]
        result.append(kelvin)
        result.append(fahrenheit)
    """

# ====== 测试代码（自己加的）======
if __name__ == "__main__":
    sol = Solution()
    result = sol.convertTemperature(36.50)
    print(result)