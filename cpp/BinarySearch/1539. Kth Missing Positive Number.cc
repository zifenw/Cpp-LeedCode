#include <vector>
using namespace std;
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int left = 0;
        int right = arr.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int missing = arr[mid] - mid - 1;
            if (missing < k) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        // left 指向的是数组中第一个满足“缺失数数量大于或等于 k”的位置
        // 换句话说，left 是第 k 个缺失数应该插入的位置
        // 这 k 个数正常都应该插入到 left 之前
        // left 之前有 left 个数
        // left + k 就是插入后 left 之前的个数 [1, left + k]
        // 最后一个是 left + k;
        return left + k;
    }
};