#include <string>
#include <vector>
using namespace std;
typedef long long ll;
class Solution {
public:
    // Convert a num to str in base-k
    string toBaseK (ll num, int k) {
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
        while (i < j) {
            if (s[i++] != s[j--]) {
                return false;
            }
        }
        return true;
    }

    ll kMirror(int k, int n) {
        vector <ll> result;
        int length = 1;
        while (result.size() < n) {
            int mid = (length - 1) / 2; 
            int start = pow(10, mid);
            int end = pow(10, mid + 1); 
            string rs;

            for (int half = start; half < end && result.size() < n; half++) {
                string s = to_string(half); 
                if (length % 2 != 0) {              // Odd   
                    rs = s.substr(0, s.size()-1); 
                } else {                            //Even     
                    rs = s;                     
                }
                reverse(rs.begin(), rs.end());
                string full = s + rs; 
                ll num = stoll(full);
                if (isPalindrome(toBaseK(num, k))) {
                    result.push_back(num);
                }
            }
            length++;
        }

        ll sum = 0;
        for (ll num : result)
            sum += num;
        return sum;
    }
};