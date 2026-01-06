#include <vector>
using namespace std;
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int currentEnd = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (i+ nums[i] > currentEnd) {
                currentEnd = i+ nums[i];
            }
            if (currentEnd >= nums.size() - 1) {
                break;
            }
            if (i == currentEnd && nums[currentEnd] == 0) {
                return false;
            }
        }
        return true;
    }
};