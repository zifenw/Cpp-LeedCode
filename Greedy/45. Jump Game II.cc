#include <vector>
using namespace std;
class Solution {
public:
    int jump(vector<int>& nums) {
        // int index = 0;
        // int length = nums.size();
        // int maxJump;
        // int newJump;
        // int maxJumpIdx;
        // int output = 0;
        // while (index < length) {
        //     maxJump = 0;
        //     for (int i = 1; i <= nums[index]; i++) {
                
        //         newJump = nums[index + i] + i;
        //         if (newJump > maxJump) {
        //             maxJump = newJump;
        //             maxJumpIdx = i;
        //         }
        //     }
        //     index += maxJumpIdx;
        //     output++;
        // }
        // return output;

        int jumps = 0;
        int currentEnd = 0;
        int farthest = 0;
        for (int i = 0; i < nums.size() - 1; i++) {
            farthest = max(farthest, i + nums[i]);

            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest;
            }

            if (currentEnd >= nums.size() - 1) 
                break;
        }
        return jumps;
    }
};