## 26. Remove Duplicates from Sorted Array
- C++ 中的 `std::vector` 和 Java 中的 `ArrayList`类似
- `nums.empty()`
- `nums.size()`
- `nums[i]`

## 27. Remove Element
- 和26相同，我们可以创建一个index作为return value的“指针”，另一个index进行原先array的遍历。像打字机一样如果符合要求就加入拷贝入return array，再移动指针；如果不符合要求，则查看下一个
- CPP == c++

## 66. Plus One
- `vector.begin()`
- `vector.end()`
- `digits.insert(digits.begin(), 1)`

## 88. Merge Sorted Array
❌错误代码：没有正确考虑 nums1 末尾的 0 值，需要从 后向前 归并，避免额外的插入操作
```c++
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int p1 = 0, p2 = 0;
        while (p2 < nums2.size()) {
            if (nums2[p2] <= nums1[p1]) {
                nums1.insert(nums1.begin() + p1, nums2[p2]);
                p1++;
            }
            p2++;
        }
    }
```
- don't need use `vector.size()` if not need run O(n)
- `auto rit1 = nums1.rbegin() + n;` auto 让编译器自动推导变量的类型，减少代码冗余，提高可读性; rbegin() 是 反向迭代器（reverse iterator），它指向 nums1 最后一个元素（即 nums1.end() - 1）。