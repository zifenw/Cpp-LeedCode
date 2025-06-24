# Sort 
c++ 的底层sort是一个叫 Introsort 的混合排序算法

```cpp
// 升序排序（从小到大）
sort(nums.begin(), nums.end());
//降序排序（从大到小）
sort(nums.begin(), nums.end(), greater<int>());



// 自定义比较函数（普通函数）
bool customCompare(int a, int b) {
    return a > b;  // 降序排序
}

vector<int> nums = {5, 2, 8, 1};
sort(nums.begin(), nums.end(), customCompare);



// Lambda 表达式排序
sort(nums.begin(), nums.end(), [](int a, int b) {
    return a > b;  // 降序
});
```