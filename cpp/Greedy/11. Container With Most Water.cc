#include <vector>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maxArea = 0;
        while (left < right) {
            int currentArea = (right - left) * min(height[left],height[right]);
            if ( currentArea > maxArea) {
                maxArea = currentArea;
            }
            if (height[left] < height[right]) {
                left++;
            } else {
                right++; //如果更高的一个pointer都不能增加maxArea，低的pointer也不可能
            }
        }
        return maxArea;
    }
};

//