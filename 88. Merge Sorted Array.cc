#include <vector>
using namespace std;
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int p1 = m - 1;  // point to the last non-zero element in nums1
        int p2 = n - 1;  // point to the end of nums2
        int p = m + n - 1;  // don't need use vector.size(), point to the end of nums1
        while (p1 >= 0 && p2 >= 0) {
            if (nums2[p2] >= nums1[p1]) {
                nums1[p] = nums2[p2];
                p2--;
            } else {
                nums1[p] = nums1[p1];
                p1--;
            }
            p--;
        }
        // if p2 没有剩余就完成merge；p2还有剩余就补充进p1
        while (p2 >= 0) {
            nums1[p] = nums2[p2];
            p2--;
            p--;    
        }
    }
};