#include <vector>
using namespace std;
class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int neg = my_lower_bound(nums, 0);
        int pos = nums.size() - my_upper_bound(nums, 0);
        return max(pos, neg);
    }
private:
    int my_upper_bound(vector<int>& nums, int target) {
        int left = 0, right = nums.size();  // 注意 right 初始化为 size()
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > target) {
                right = mid;  // 收缩右边界
            } else {
                left = mid + 1;  // 向右查找
            }
        }
        return left;  // 返回第一个 > target 的索引
    }
    int my_lower_bound(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};