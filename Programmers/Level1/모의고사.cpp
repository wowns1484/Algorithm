#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> p1 = {1,2,3,4,5};
    vector<int> p2 = {2,1,2,3,2,4,2,5};
    vector<int> p3 = {3,3,1,1,2,2,4,4,5,5};
    map<int, int> m;
    m.insert(pair<int, int>(1, 0));
    m.insert(pair<int, int>(2, 0));
    m.insert(pair<int, int>(3, 0));
    
    for(int i = 0; i < answers.size(); i++)
    {
        if(p1[i % 5] == answers[i])
            m[1]++;
        if(p2[i % 8] == answers[i])
            m[2]++;
        if(p3[i % 10] == answers[i])
            m[3]++;
    }
    
    int largest = max(max(m[1], m[2]), m[3]);
    
    for(auto iter = m.begin(); iter != m.end(); iter++)
    {
        if(iter->second == largest)
            answer.push_back(iter->first);
    }
    
    return answer;
}