#include <string>
#include <vector>

using namespace std;

int solution(int n)
{
    bool *arr = new bool[n + 1]{false};
    int answer = 0;

    for(int i = 2; i <= n; i++)
    {
        for(int j = 2; j*i <= n; j++)
            if(arr[i*j] == false)
                arr[i*j] = true;
    }

    for(int i = 2; i <= n; i++)
    {
        if(arr[i] == false)
            answer++;
    }

    return answer;
}