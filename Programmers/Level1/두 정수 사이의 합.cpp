#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    int small = a < b ? a : b;
    int big = a < b ? b : a;
    
    for(int i = small; i <= big; i++)
        answer += i;
    
    return answer;
}