# 2081. Sum of k-Mirror Numbers

A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

Given the base k and the number n, return the sum of the n smallest k-mirror numbers.

### 进制转换
```cpp
    // Convert a num to str in base-k
    string toBaseK (long long num, int k) {
        string res;
        while (num > 0) {
            res += (char)('0' + num % k);
            num /= k;
        }
        reverse(res.begin(), res.end());
        return res;
    }
    // 9 % 2 = 1 -> 1
    // 9 / 2 = 4
    // 4 % 2 = 0 -> 01
    // 4 / 2 = 2
    // 2 % 2 = 0 -> 001
    // 2 / 2 = 1
    // 1 % 2 = 1 -> 1001
    // 1 / 1 = 0 END
    // res += 5; 会把 ASCII 码为 5 的控制字符加入字符串（不是 '5'）
    // '0' + num % k 正确，将数字转换为字符 '0'~'9'
```

```cpp
if (digit < 10)
    res += '0' + digit;
else
    res += 'A' + (digit - 10);  // 用大写字母表示10~15
```

### 镜像检测(回文数)
```cpp
    // check if the str is a palindrome
    bool isPalindrome (const string& s) {
        int i = 0, j = s.size() - 1;
        while (i > j) {
            if (s[i++] != s[j--]) {
                return false;
            }
        }
        return true;
    }
    // String can be used as the Vector
    // i++ and j-- is smart
```