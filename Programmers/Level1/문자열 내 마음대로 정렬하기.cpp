#include <string>
#include <vector>
#include <iostream>

using namespace std;

void swap(vector<string> &strings, int a, int b)
{
    string temp = strings[a];
    strings[a] = strings[b];
    strings[b] = temp;
}

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
    
    for(int i = 1; i < strings.size(); i++)
    {
        for(int j = i; j > 0; j--)
        {
            if(strings[j][n] < strings[j - 1][n] || 
               (strings[j][n] == strings[j - 1][n] && strings[j] < strings[j - 1]))
                swap(strings, j, j - 1);
        }
    }
    
    for(auto elem : strings)
        answer.push_back(elem);
    
    return answer;
}