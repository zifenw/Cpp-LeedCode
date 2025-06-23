#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    // Convert a num to str in base-k
    string toBaseK (long long num, int k) {
        string res;
        while (num > 0) {
            res += (char)('0' + num % k);
            num /= k;
        }
        reverse(res.begin(), res.end());
        return res;
    }

    // check if the str is a palindrome
    bool isPalindrome (const string& s) {
        int i = 0, j = s.size() - 1;
        while (i > j) {
            if (s[i++] != s[j--]) {
                return false;
            }
        }
        return true;
    }

    long long kMirror(int k, int n) {
        vector <long long> result;
        int length = 1;
        while (result.size() < n) {
            // Odd length

            // Even length

            length++;
        }



        long long sum = 0;
        for (long long num : result)
            sum += num;
        return sum;
    }
};