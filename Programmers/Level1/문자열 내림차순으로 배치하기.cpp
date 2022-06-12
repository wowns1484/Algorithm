#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    
    for(int i = 1; i < s.size(); i++)
    {
        for(int j = i; j > 0; j--)
        {
            if(s[j] > s[j - 1])
            {
                char c = s[j];
                s[j] = s[j - 1];
                s[j - 1] = c;
            }
        }
    }
    
    answer = s;
    
    return answer;
}