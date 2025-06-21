# 11. Container With Most Water
Return the maximum amount of water a container can store.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

**two pointer problem, check which pointer is greater during iterate**

# 44. Wildcard Matching
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character (*not including the empty sequence*).
'*' Matches any sequence of characters (including the empty sequence).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

longer example:
s = "abcdd"
p = "a*c*d"

Greedy:
**set pointer i and j for s and p; set startIdx and matchIdx; Iterate i checking char are same or p[j] is ?; when p[j] is *, set * be '' first and cotinue checking(use starIdx and MatchIdx to lable); when not matching check do we have star, if we have matchIdx++ and cotinue check, else just return false; Iterate j for the remain p, if it's * just continue, else just out the iterate; return the j == p.length()**

# 45. Jump Game II

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

**不用真的跳，只需记录你当前这次跳跃最多能跳多远（farthest）;一旦你到了当前能跳的边界（currentEnd），就必须跳一次，跳到 farthest**

**At each step, greedily track the farthest position reachable within the current jump range. When you reach the end of that range, increment the jump count and update the range to the farthest position. Repeat until the end is covered.**

# 55. Jump Game