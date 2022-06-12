#include <string>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int cnt_p = 0, cnt_y = 0;
    
    for(char c : s)
    {
        if(c == 'p' || c == 'P' || c == 'y' || c == 'Y')
            (c == 'p' || c == 'P') ? cnt_p++ : cnt_y++;
    }

    if(cnt_p != cnt_y)
        answer = false;
        
    return answer;
}