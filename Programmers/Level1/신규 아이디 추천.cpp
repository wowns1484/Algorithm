#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {
    string answer = "";
    string temp = "";
    
    // 1, 2단계
    for(char word : new_id)
    {
        if(word >= 'A' && word <= 'Z')
            word += 'a' - 'A';
        
        if((word >= 'a' && word <= 'z') || (word <= '9' && word >= '0') || word == '-' || word == '_' || word == '.')
            temp += word;
    }
    
    // 3단계
    for(int i = 0; i < temp.size(); i++)
    {
        if(temp[i] == '.' && temp[i + 1] == '.')
            continue;
        else
            answer += temp[i];
    }
    
    // 4단계
    if(answer[0] == '.') 
        answer.erase(0, 1);
    if(answer[answer.size() - 1] == '.')
        answer.erase(answer.size() - 1, 1);
    
    // 5단계
    if(answer == "")
        answer = "a";
    
    // 6, 7단계
    if(answer.size() > 15)
    {
        answer.erase(15, answer.size());
        
        if(answer[answer.size() - 1] == '.')
            answer.erase(answer.size() - 1, 1);
    }
    else if(answer.size() < 3)
    {
        while(answer.size() < 3)
            answer.push_back(answer[answer.size() - 1]);
    }

    return answer;
}