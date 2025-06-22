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