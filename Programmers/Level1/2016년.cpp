#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    vector<string> weeks = {"THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"};
    string answer = "";
    int day = 0;
    
    if(a > 1)
    {
        for(int i = 1; i < a; i++)
        {
            if(i == 4 || i == 6 || i == 9 || i == 11)
                day += 30;
            else if(i == 2)
                day += 29;
            else
                day += 31;
        }
    }
    day += b;
    
    answer = weeks[day % 7];
    
    return answer;
}