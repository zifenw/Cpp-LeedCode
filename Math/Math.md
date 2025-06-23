# 2081. Sum of k-Mirror Numbers

A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

Given the base k and the number n, return the sum of the n smallest k-mirror numbers.

### **typedef long long ll;**

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

### 位数遍历
```cpp
    while (result.size() < n) {
        // Odd length                            // length 5 
        for (int half = pow(10, (length - 1) / 2);
            result.size() < n && half < pow(10, (length + 1) / 2);
            ++half) {                            // from 10^2 to 10^3
            string s = to_string(half);          // s = "123"
            string rs = s.substr(0, s.size()-1); // rs = "12"（去掉中间重复字符）
            reverse(rs.begin(), rs.end());       // rs = "21"
            string full = s + rs;                // full = "12321"（奇数长度文）
            long long num = stoll(full);         // 字符串转数字
        }
        // Even length                           // length 4
        for (int half = pow(10, length / 2 - 1); 
            result.size() < n && half < pow(10, length / 2);
            ++half) {                            // from 10^1 to 10^2
            string s = to_string(half);          // s = "12"
            string rs = s;                     
            reverse(rs.begin(), rs.end());       // rs = "21"
            string full = s + rs;                // full = "1221"
            long long num = stoll(full);
        }
        length++;
    }
// for loop中的 result.size() < n 帮助代码退出 while loop
// (length - 1) / 2 is 

// Update:
    while (result.size() < n) {
        int mid = (length - 1) / 2; 
        int start = pow(10, mid);
        int end = pow(10, mid + 1); 
        string rs;

        for (int half = start; half < end && result.size() < n; half++) {
            string s = to_string(half); 
            if (length % 2 != 0) {              // Odd   
                rs = s.substr(0, s.size()-1); 
            } else {                            //Even     
                rs = s;                     
            }
            reverse(rs.begin(), rs.end());
            string full = s + rs; 
            long long num = stoll(full);
            if (isPalindrome(toBaseK(num, k))) {
                result.push_back(num);
            }
        }
        length++;
    }
```