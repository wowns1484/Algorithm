#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<int> temp;
    
    for(int i = n; i > 0; i /= 3)
        temp.push_back(i % 3);
    
    
    for(int i = 0; i < temp.size(); i++)
    {
        int square = temp.size() - i - 1, elem = 1;
        while(square > 0)
        {
            elem *= 3;
            square--;
        }
        answer += elem*temp[i];
    }
    
    return answer;
}