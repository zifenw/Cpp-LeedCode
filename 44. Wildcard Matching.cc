#include <string>
using namespace std;
class Solution {
public:
    bool isMatch(string s, string p) {
        int i = 0, j = 0;
        int starIdx = -1;
        int matchIdx = 0;
        while (i < s.length()) {
            if (j < p.length() && (p[j] == s[i] || p[j] == '?')) {
                i++;
                j++;
            } else if (j < p.length() && p[j] == '*') {
                matchIdx = i;
                starIdx = j;
                j++;                // 先假设 * 匹配0个字符
            } else if (starIdx != -1) {
                j = starIdx + 1;    // j退到 * 后一位
                matchIdx++;
                i = matchIdx;       // 让 * 多匹配一个字符
            } else {                // starIdx = -1 no star in pattern
                return false;       // and s not match p
            }
        }
        while (j < p.length() && p[j] == '*') {
            j++;
        }

        return j == p.length();
    }
};