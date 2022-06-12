#include <string>
#include <vector>

using namespace std;

bool solution(string s) {
    bool answer = false;
    
    if(s.size() == 4 || s.size() == 6)
    {
        answer = true;
        for(char c : s)
            if(isdigit(c) == 0)
            {
                answer = false;
                break;
            }
    }
    
    return answer;
}