
#include <iostream>
#include <string>
#include <unordered_map>
#include <cstring>

using namespace std;

void printMap(unordered_map<char, int> m)
{
    for (const auto & [k, v] : m) 
    {
        cout << k << ",";
    }

    cout << endl;
}

class Solution {
public:
    int lengthOfLongestSubstring_unordered_map(string s) {
        unordered_map<char, int> m;
        int longest = 0;

        const char* pStart = s.c_str();
        const char* const pEnd = pStart + s.length();
        const char* pCurr = pStart;

        while (pCurr < pEnd) {
            const char c = *pCurr;
            if (m.find(c) != m.end()) {
                // repeat found
                longest = (longest > m.size()) ? longest : m.size(); // save map contents if longest
                m.clear();
                pCurr = ++pStart;
            }
            else {
                ++pCurr;
                m[c] = 1;
            }
        }
        return longest = (longest > m.size()) ? longest : m.size();
    }    

    int lengthOfLongestSubstring_noalloc(string s) {
        
        int ascii[128] = {};
        int longest = 0;

        const char* pStart = s.c_str();
        const char* const pEnd = pStart + s.length();
        const char* pCurr = pStart;

        while (pCurr < pEnd) {            
            const char c = *pCurr;
            if (ascii[c]) {
                // repeat found
                const int size = getSize(ascii);
                longest = max(longest, size);
                memset(ascii, 0, sizeof(ascii));
                pCurr = ++pStart;
            }
            else {
                ++pCurr;
                ascii[c] = 1;
            }
        }
        const int size = getSize(ascii);
        return max(longest, size);
    }

    inline int getSize(const int (&ascii) [128])
    {
        int size = 0;
        for (const auto i : ascii) {
            size += i;
        }
        return size;
    }

    int lengthOfLongestSubstring_nyon(string s) {
        char lookup[128];
        int longest = 0;
        int current = 0;
        char c;
        const int count = s.size();
        for(int i = 0; count > i; ++i) {
            c = s[i];
            memset(lookup, 0, sizeof(char) * 128);
            lookup[c] = 1;
            current = 1;
            
            for (int j = i + 1; count > j; ++j) {
                c = s[j];
                if (lookup[c] != 0) {
                    break;
                }
                lookup[c] = 1;
                current++;
            }
            
            if (longest < current) {
                longest = current;
            }
        }
        
        if (longest < current) {
            return current;
        }
        
        return longest;
    }
};

void printResult(string str)
{    
    Solution s;
    auto len = s.lengthOfLongestSubstring_nyon(str);
    cout << "length of longest substring for " << str << " is " << len << endl;
}

int main()
{
    printResult(" ");
    printResult("ab");
    printResult("abcabcbb");
    printResult("dvdf");
    printResult("asjrgapa");

    return 0;
}