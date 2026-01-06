#include <vector>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;  // Handle edge case for empty array
        
        int i = 0;  // Pointer to track the position of unique elements
        for (int j = 1; j < nums.size(); j++) {
            if (nums[j] != nums[i]) {  // Found a new unique element
                i++;  // Move i to the next position
                nums[i] = nums[j];  // Update the element at position i
            }
        }
        return i + 1;  // Return the number of unique elements
    }
};