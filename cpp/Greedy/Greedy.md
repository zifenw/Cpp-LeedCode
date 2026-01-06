# 11. Container With Most Water
Return the maximum amount of water a container can store.   
Input: height = [1,8,6,2,5,4,8,3,7]   
Output: 49   

>two pointer problem, check which pointer is greater during iterate

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
>set pointer i and j for s and p; set startIdx and matchIdx; Iterate i checking char are same or p[j] is ?; when p[j] is *, set * be '' first and cotinue checking(use starIdx and MatchIdx to lable); when not matching check do we have star, if we have matchIdx++ and cotinue check, else just return false; Iterate j for the remain p, if it's * just continue, else just out the iterate; return the j == p.length()

# 45. Jump Game II

Example 1:

Input: nums = [2,3,1,1,4]  
Output: 2  
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

>不用真的跳，只需记录你当前这次跳跃最多能跳多远（farthest）; 一旦你到了当前能跳的边界（currentEnd），就必须跳一次，跳到 farthest

>At each step, greedily track the farthest position reachable within the current jump range. When you reach the end of that range, increment the jump count and update the range to the farthest position. Repeat until the end is covered.

# 55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]  
Output: true  
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.  
Example 2:  

Input: nums = [3,2,1,0,4]  
Output: false  
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

>不用真的跳，检查是否到达当前能跳的边界currentEnd（i == currentEnd）和currentEnd是否为0，直到reach最后一个index

# 122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]  
Output: 7  
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.  
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.  
Total profit is 4 + 3 = 7.  
Example 2:  

Input: prices = [1,2,3,4,5]  
Output: 4  
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.  
Total profit is 4.  
Example 3:  

Input: prices = [7,6,4,3,1]  
Output: 0  
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.  

>简单的Sell Stock可当天买卖，所以只要有prices[i] < prices[i+1]就可以加入profit

>但要注意Base case[1], 注意不要超出arraysize，i < prices.size() - 1和初始int profit = 0;

# 134. Gas Station

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]  
Output: 3  
Explanation:  
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4  
Travel to station 4. Your tank = 4 - 1 + 5 = 8  
Travel to station 0. Your tank = 8 - 2 + 1 = 7  
Travel to station 1. Your tank = 7 - 3 + 2 = 6  
Travel to station 2. Your tank = 6 - 4 + 3 = 5  
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.  
Therefore, return 3 as the starting index.  


**只要currentGas小于0，说明从该站之前经过遍历的任意一个车站出发都不可以满足要求；只要totalGas最终小于0，说明总有一个站可以作为起点而满足要求**

> **Hint** 平面直角坐标系中考虑任意曲线记录currentGas，从0开始如果一个非负曲线在某一个x值小于等于0的话取之前任意点为起始点（x轴会上移）都会导致到达该点时小于0。而如果低于x轴会重新记录起始点。

> **Hint** 平面直角坐标系中考虑任意曲线记录totalGas，如果该曲线最终为非负。我们可以选择从曲线最低点作为起始点，新的一圈不会有任意点小于该最低点，也就是小于0

>**return totalGas > 0 ? start : -1;** (判断标准 ? true返回值 : false返回值)

# 179. Largest Number
**使用sort对于[](string a, string b) { return a + b > b + a; }**

**特殊情况：全是0，排序后第一个是"0" 就说明结果是 "0"**


