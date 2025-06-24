#include <string>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> strNums;
        for (int num : nums) {
            strNums.push_back(to_string(num));
        }

        sort(strNums.begin(), strNums.end(),
             [](string a, string b) { return a + b > b + a; });

        // 特殊情况：全是0，排序后第一个是"0" 就说明结果是 "0"
        if (strNums[0] == "0") return "0";

        string result;
        for (const string& s : strNums) {
            result += s;
        }

        return result;
    }
};