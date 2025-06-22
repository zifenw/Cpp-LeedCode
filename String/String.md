# 2138. Divide a String Into Groups of Size k

Example 1:  
Input: s = "abcdefghi", k = 3, fill = "x"  
Output: ["abc","def","ghi"]  

Example 2:  
Input: s = "abcdefghij", k = 3, fill = "x"  
Output: ["abc","def","ghi","jxx"]  

---

>**s.substr(startIdx, length)** get the substr of the str 

string group = s.substr(i, k);

>**s.append(num, char)** add some char after str

group.append(k - groupsize(), fill);

>**s.size()** size of the string

>**vector<type> name** initialize the vector

vector\<string\> result;

>**vector.push_back()** add element after vector

