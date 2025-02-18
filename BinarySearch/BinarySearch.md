## 2529. Maximum Count of Positive Integer and Negative Integer
- 直接遍历 (O(n))
```cpp
    int maximumCount(vector<int>& nums) {
        int pos = 0, neg = 0;
        for (int num : nums) {
            if (num > 0) pos++;
            else if (num < 0) neg++;
        }
        return max(pos, neg);
    }
```
- Binary Search
`lower_bound(begin, end, target)` 返回第一个 >= target 的元素索引  
`upper_bound(begin, end, target)` 返回第一个 > target 的元素索引

```cpp
    // 找到第一个 >= 0 的元素索引 (即负数的个数)
    int neg = lower_bound(nums.begin(), nums.end(), 0) - nums.begin();

    // 找到第一个 > 0 的元素索引
    int pos = nums.end() - upper_bound(nums.begin(), nums.end(), 0);
```
❌`int neg = lower_bound(nums.begin(), nums.end(), 0);`
会产生 compile error，因为 lower_bound 返回的是 迭代器（`vector<int>::iterator`），而 neg 是一个 `int`，导致类型不匹配。

lower_bound(nums.begin(), nums.end(), 0) 返回 指向第一个大于等于 0 的元素的迭代器。   
nums.begin() 是 nums 的起始迭代器。   
指针减法（iterator - iterator）的结果是 索引，它表示 lower_bound 返回的迭代器相对于 nums.begin() 的偏移量。


- while循环 while(left < right){}
  - 在whileloop中定义mid，可以使每次循环更新mid
  - 边界收缩: if (what you want to get) {right/left = mid} since mid is possible become the target
  - else {left/right = mid + 1} mid cannot be a target so skip in next loop
- `max(pos, neg)`; same as `(pos >= neg) ? pos : neg`;

## 2540. Minimum Common Value
| Approach        | Time Complexity | Space Complexity | Best When?                           |
|-----------------|-----------------|------------------|--------------------------------------|
| Two-Pointer     | O(N + M)        | O(1)             | Best overall for sorted arrays      |
| Binary Search   | O(N log M)      | O(1)             | Good if nums1 is much smaller than nums2 |
| Set-based       | O(N + M)        | O(N)             | Good for unsorted arrays            |

```cpp
// two pointer approach
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int i = 0, j = 0;
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] == nums2[j]) return nums1[i]; // Found the smallest common element
            else if (nums1[i] < nums2[j]) i++; // Move i forward
            else j++; // Move j forward
        }
        return -1; // No common element
    }
// binary search approach
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        for (int num : nums1) {
            if (binary_search(nums2.begin(), nums2.end(), num)) {
                return num; // Found the smallest common number
            }
        }
        return -1; // No common number found
    }
// set appoach
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> s(nums1.begin(), nums1.end()); // Insert nums1 into set
        for (int num : nums2) {
            if (s.count(num)) return num; // If num exists in set, return it
        }
        return -1; // No common element found
    }
```
- 在C++中，如果if、else if或while等控制流语句只包含一条语句，则可以省略花括号{}
- `binary_search(first, last, value);` works only for sorted container, return ture or false to find or not
- `#include <set>` 有序的容器，它以特定的顺序维护其元素，默认情况下通常按升序排序
- `#include <unordered_set>` 无序的容器，它不保证其元素的任何特定顺序。它通常使用哈希表来实现。
- `insert()`, `erase()`(remove), `size()`, `empty()`, `clear()`(removeAll), `count()` (contain) return bool, `find()` return index, `lower_bound()`, `upper_bound()`, `swap()`