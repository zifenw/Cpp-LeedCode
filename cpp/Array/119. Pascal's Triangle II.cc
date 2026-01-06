#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row(rowIndex + 1, 1);
        long long val = 1; // Start with first element (always 1)

        for (int k = 1; k <= rowIndex; k++) {
            val = val * (rowIndex - k + 1) / k;
            row[k] = val;
        }

        return row;
    }
};
/*
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row(rowIndex + 1, 1); // Initialize the row with 1s

        for (int i = 1; i < rowIndex; i++) {
            for (int j = i; j > 0; j--) {
                row[j] += row[j - 1];  // Compute new values from right to left
            }
        }
        return row;
    }
};
*/