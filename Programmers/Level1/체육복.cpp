#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> temp(n, 1);
    
    for(int elem : lost)
        temp[elem - 1] -= 1;
    
    for(int elem : reserve)
        temp[elem - 1] += 1;
    
    for(int i = 0; i < n; i++)
    {
        if(temp[i] == 0 && temp[i + 1] == 2)
        {
            temp[i] += 1;
            temp[i + 1] -= 1;
        }
        else if(temp[i] == 0 && temp[i - 1] == 2)
        {
            temp[i - 1] -= 1;
            temp[i] = 1;
        }
    }
    
    for(int elem : temp)
        if(elem > 0)
            answer++;
    
    return answer;
}