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

## 108. Convert Sorted Array to Binary Search Tree
- 标准的递归创建BST
```cpp
    TreeNode* buildBST(vector<int>& nums, int left, int right) {
        if (left > right) return nullptr;

        int mid = left + (right - left) / 2;
        TreeNode* root = new TreeNode(nums[mid]);

        root->left = buildBST(nums, left, mid - 1);
        root->right = buildBST(nums, mid + 1, right);
        
        return root;
    }
```
- BS重点是left, right, mid=left+(right-left)/2

## 118. Pascal's Triangle
**Resize OR Declaring a vector**
**Push_back OR array[i][j]**
```cpp
vector<int> vec;
vector<int> vec2(5, 0);
vector<int> vec3 = {1, 2, 3, 4, 5};

// this problem
vector<vector<int>> triangle(numRows);

//resize
vector<int> vec;  // Initially empty
vec.resize(5, 0);
vec.resize(10, 1);
// Result after first resize: [0, 0, 0, 0, 0]
// Final result: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
// this problem
triangle[i].resize(i + 1, 1);
```

## 119. Pascal's Triangle II
What the f**k!!!
Just math!!!

## 121. Best Time to Buy and Sell Stock
找到前后顺序固定的最大差值(利润)    
可以更具给出的example遍历进行条件判定    

## 136. Single Number (XOR WHAT???)
查找唯一的单独数字，其它都是pair  
```CPP
    int singleNumber(vector<int>& nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
```
4⊕1⊕2⊕1⊕2  
**XOR**    
100 ^ 001 = 101  
101 ^ 010 = 111  
111 ^ 001 = 110  
110 ^ 010 = 100  

a⊕a=0 (Any number XOR itself is 0)
a⊕0=a (Any number XOR 0 remains unchanged)

```
nums = [4,1,2,1,2]
Step-by-step XOR:
4 ⊕ 1 ⊕ 2 ⊕ 1 ⊕ 2
= (4 ⊕ (1 ⊕ 1) ⊕ (2 ⊕ 2))
= (4 ⊕ 0 ⊕ 0)
= 4
```

## 169. Majority Element
查找element中超过一半的大多数  
**Boyer-Moore Voting Algorithm**
```cpp
    int candidate = 0, count = 0;

    for (int num : nums) {
        if (count == 0) {
            candidate = num;
        }
        count += (num == candidate)? 1 : -1;
    }

    return candidate;
```
当 count 为 0 时，算法会选择一个新的候选元素。实际上，count 变为 0 说明候选元素已经被其他元素“抵消”掉了，此时候选元素会被替换。

如果 x 是多数元素，它会最终在计数上占优势。即使有其他元素也与 x 相同次数地出现，x 会由于它出现次数较多而在计算过程中维持候选身份。

对于多数元素 x，它的出现次数超过其他元素的总和，因此无论其他元素如何抵消，x 的最终出现次数将始终超过任何其他候选元素。(正真的candidate的数量如果大于一半一定可以与所有不是的element相消后仍有剩余)  

## 217. Contains Duplicate (hashtable/sorting)
**find() for unsorted_set**
find() 和 end() 都是iterator指针
```
If the element is found:

find() returns an iterator pointing to the element in the set.

For example: if num exists in the set, find(num) will return a valid iterator pointing to that element.

If the element is not found:

find() returns an iterator to seen.end(), which is a special iterator that marks the end of the container (i.e., it doesn't point to a valid element).
```
`seen.end()` points just beyond the last element
`seen.insert(num)`
`seen.find(num)`

we can also sort directly:
```cpp
    bool containsDuplicate(vector<int>& nums) {
     sort(nums.begin(),nums.end());
     for(int i=0;i<nums.size()-1;i++){
        if(nums[i]==nums[i+1]){
          return true;
          break;
        }
        
     }
     return false;

    }
```
## 219. Contains Duplicate II